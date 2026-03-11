import pandas as pd
import random
from datetime import datetime, timedelta

# lista que vai guardar os dados
dados = []

# horário inicial
inicio = datetime.now()

# vamos gerar 50 registros
for i in range(50):

    timestamp = inicio + timedelta(minutes=i*5)

    latencia = random.randint(15, 120)

    if latencia > 100:
        status = "offline"
    else:
        status = "online"

    dados.append({
        "timestamp": timestamp,
        "latencia_ms": latencia,
        "status": status
    })

df = pd.DataFrame(dados)

df.to_csv("dados_rede.csv", index=False)

print("Dataset criado com sucesso!")
print(df.head())