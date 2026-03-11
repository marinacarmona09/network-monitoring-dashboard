import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Mini Dashboard Rede", layout="wide")

st.title("Mini Dashboard - Monitoramento de Rede Simples")

# 1) Ler o CSV
df = pd.read_csv("dados_rede.csv")

# 2) Transformar timestamp em data/hora
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Ordenar os dados pelo tempo
df = df.sort_values("timestamp")

# 3) KPIs
total = len(df)
pct_offline = (df["status"].eq("offline").mean() * 100) if total else 0
lat_media = df["latencia_ms"].mean() if total else 0
lat_max = df["latencia_ms"].max() if total else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Registros", f"{total}")
c2.metric("Offline (%)", f"{pct_offline:.1f}%")
c3.metric("Latência média (ms)", f"{lat_media:.1f}")
c4.metric("Latência máxima (ms)", f"{lat_max:.0f}")

st.divider()

# 4) Gráfico de latência ao longo do tempo com Plotly
st.subheader("Latência ao longo do tempo")

fig_latencia = px.line(
    df,
    x="timestamp",
    y="latencia_ms",
    color="status",  # adiciona cor baseada no status
    title="Latência ao longo do tempo",
    markers=True,
    color_discrete_map={
        "online": "green",
        "offline": "red"
    }
)
fig_latencia.update_layout(
    xaxis_title="Data e hora",
    yaxis_title="Latência (ms)",
    legend_title="Status da Rede") 

st.plotly_chart(fig_latencia, use_container_width=True)

# 5) Contagem online vs offline
st.subheader("Online vs Offline")

status_counts = df["status"].value_counts().reset_index()
status_counts.columns = ["status", "quantidade"]

fig_status = px.bar(
    status_counts,
    x="status",
    y="quantidade",
    color="status",
    text="quantidade",
    color_discrete_map={
        "online": "green",
        "offline": "red"}
)

fig_status.update_layout(
    xaxis_title="Status",
    yaxis_title="Quantidade",
    xaxis_tickangle=0)

st.plotly_chart(fig_status, use_container_width=True)

# 6) Mostrar tabela
with st.expander("Ver dados tabela"):
    st.dataframe(df)