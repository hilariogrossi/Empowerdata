import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly

codigo = input('Digite o código de ação: ')

dados = yf.Ticker(codigo).history('2y')

#print(dados.head())
#print(dados.shape)

# Tratamento de Dados
# Série temporal
# Resetar o índice

treinamento = dados.reset_index()
#print(treinamento)

#print(treinamento['Date'])
#print(treinamento[['Date', 'Close']])

# Extraindo apenas a data da coluna Date
#treinamento = dados.reset_index()
treinamento['Date'] = treinamento['Date'].dt.date

# Filtra meus dados
#print(treinamento)

colunas = ['Date', 'Close']
treinamento = treinamento[colunas]
#print(treinamento)

#print(treinamento.columns)

# Alterar os nomes das colunas
treinamento.columns = ['ds', 'y']
#print(treinamento)

# Criar o modelo
modelo = Prophet()

# Treinar o modelo
modelo.fit(treinamento)

# Gerando Previsões
periodo = modelo.make_future_dataframe(90)
#print(periodo.head())

previsoes = modelo.predict(periodo)
#print(previsoes)

# Visualização de Dados
grafico = plot_plotly(modelo, previsoes)

grafico.show()
