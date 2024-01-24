## Problema a ser resolvido - passo a passo
# - Buscar automaticamente os dados das ações
# - Gerar as análises de forma automática
# - Enviar um email para o nosso gestor

### Passo 1 - Buscar automaticamente os dados das ações

import yfinance
import pyautogui
import pyperclip

codigo = input('Digite o código da ação desejada: ')
dados = yfinance.Ticker(codigo).history('6mo')
#print(dados)
fechamento = dados.Close

### Passo 2 - Gerar as análises de forma automática
#- Análise dos últimos seis meses
#- Cotação máxima
#- Cotação mínima
#- Cotação atual

cotacao_maxima = fechamento.max()
print(f'O valor da cotação máxima é: R$ {cotacao_maxima:.2f}')
cotacao_minima = fechamento.min()
print(f'O valor da cotação mínima é: R$ {cotacao_minima:.2f}')
cotacao_atual = fechamento[-1]
print(f'A cotação atual é: {cotacao_atual:.2f}')

### Passo 3 - Enviar um email para o nosso gestor
#- Abrir uma nova aba no navegador (ctrl + T)
#- Digitar o endereço do e-mail e dar um enter (www.gmail.com)
#- Clicar no botão escrever
#- Colocar o email do destinatário
#- Dar um tab
#- Colocar o assunto do e-mail
#- Dar um tab
#- Escrever o e-mail
#- Clicar no botão enviar

pyautogui.PAUSE(2)
pyautogui.hotkey('ctrl', 't')

pyperclip.copy('www.gmail.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')

pyautogui.click(x=100, y=100)

pyperclip.copy('Análises diárias')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

mensagem = f'''
Prezado gestor,

seguem as análises diárias dos últimos 6 meses da ação {codigo}:

Cotação máxima: R$ {cotacao_maxima:.2f}
Cotação mínima: R$ {cotacao_minima:.2f}
Cotação atual: R$ {cotacao_atual:.2f}

Qualquer dúvida fico a disposição.

Hilário Grossi de Oliveira. '''

pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(x=3120, y=977)
