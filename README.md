# Mini Dashboard de Monitoramento de Rede

Projeto simples de monitoramento de rede desenvolvido em Python utilizando Streamlit e Plotly.

O dashboard simula dados de rede e apresenta métricas como:

- Latência média
- Latência máxima
- Percentual offline
- Status online vs offline
- Visualização temporal da latência

## Criação do Dataset

Para demonstração, foi desenvolvido um script em Python responsável por gerar um dataset simulado de monitoramento de rede.

O script cria registros sequenciais ao longo do tempo, simulando medições da rede. Para cada registro são geradas informações como:
- Timestamp da medição
- Latência da rede em milissegundos
- Status da conexão (online ou offline)

Geração dos dados:

- `datetime` e `timedelta` para construir a sequência das medições
- `random` para simular variações de latência e eventuais instabilidades na rede

Esse processo permite criar um conjunto de dados para demonstrar visualizações e métricas de monitoramento de rede no dashboard.

## Preview do Dashboard
![dashboard](imagem_dashboard.png)

## Tecnologias utilizadas

- Python
- Pandas (manipulação de dados)
- Streamlit (criação do dashboard)
- Plotly (visualização interativa)
- Random (simulação)
- Datetime / Timedelta (geração da linha temporal)

## Como executar

1. Instalar dependências
pip install -r requirements.txt

2. Gerar Dataset
python dataset_rede_simples.py

3. Executar Dashboard
streamlit run dashboard.py

## Funcionalidades

- Geração de dataset simulado
- Dashboard interativo
- Desempenho da rede
