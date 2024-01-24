from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font('Arial')

pdf.image('template.png', x=0, y=0)

descricao_projeto = input('Digite a descrição do Projeto: ')
horas_previstas = input('Digite a quantidade de horas previstas: ')
valor_hora = input('Digite o valor da hora trabalhada: ')
prazo = input('Digite o prazo estimado: ')

valor_total = int(valor_hora) * int(horas_previstas)

pdf.text(115, 145, descricao_projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output('Orçamento.pdf')

print('Orçamento gerado com sucesso!')
