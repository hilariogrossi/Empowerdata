import pandas as pd
import plotly_express as px

dados = pd.read_excel('vendas.xlsx')
print(dados.head())
print(dados.tail())

# Verificando a quantidade de linhas e coluna
print(dados.shape)

# Verificando os tipos de dados
# Object = texto
print(dados.info())

#print(dados.loja)
print(dados.preco)
#print(dados.cidade)

print(dados.preco.describe())

# Total de vendas por loja
print(dados.loja.value_counts())

# Total de vendas por cidade
print(dados.cidade.value_counts())

# Total de vendas por forma de pagamento
print(dados.forma_pagamento.value_counts())

# Agrupamento de dados
# Faturamento por loja
print(dados.groupby('loja').preco.sum())

# Faturamento por estado
print(dados.groupby('estado').preco.sum().to_frame())

print(dados.groupby(['estado', 'cidade', 'loja']).preco.sum().to_frame())

# Exportando o arquivo criado acima
print(dados.groupby(['estado', 'cidade', 'loja']).preco.sum().to_excel('Faturamento-Estado-Cidade.xlsx'))

print(px.histogram(dados, x='loja', y='preco', title='Vendas por Loja', text_auto=True))

grafico = px.histogram(dados, x='loja', y='preco', title='Vendas por Loja', text_auto=True, color='forma_pagamento')

grafico.show()

grafico.write_html('grafico.html')

colunas = ['loja', 'cidade', 'estado', 'tamanho']

for coluna in colunas:
    grafico = px.histogram(dados, x=coluna, y='preco', title=f'Faturamento por {coluna}', text_auto=True, color='forma_pagamento')

    grafico.show()

    grafico.write_html(f'Grafico-{coluna}.html')

