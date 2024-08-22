from selecionador_operacao import selecionador_operacao
from executa_calculadora import executa_calculadora

saida = ''
input_um = 0
input_dois = 0
operacao = ''

while saida != 'exit':
    (input_um, input_dois, operacao) = executa_calculadora(input_um, input_dois, operacao)

    if input_um == 'exit' or input_dois == 'exit' or operacao  == 'exit':
        saida = 'exit'
        break
    if saida != 'exit':
        resultado = ''

        operacao_selecionada = selecionador_operacao(operacao)
        if callable(operacao_selecionada):
            if operacao == 'v':
                resultado = operacao_selecionada(input_um)
            else:
                resultado = operacao_selecionada(input_um, input_dois)
        else:
             print(operacao_selecionada)
    if resultado != '':
        print(f'O resultado da operação {operacao} é: {resultado}')