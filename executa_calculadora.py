from recebe_numero import recebe_numero

def executa_calculadora(input_um, input_dois, operacao):
    operacao = input(f'Digite o simbolo da operação Matemática para os valores: ')
    if operacao == 'exit':
        return input_um, input_dois, operacao

    if operacao == 'v':
        mensagem = 'Digite o primeiro valor para a operação Matemática: \n'
        input_um = recebe_numero(mensagem)
        if input_um == 'exit':
            return input_um, input_dois, operacao
        return input_um, input_dois, operacao
    
    mensagem = 'Digite o primeiro valor para a operação Matemática: \n'
    input_um = recebe_numero(mensagem)
    if input_um == 'exit':
        return input_um, input_dois, operacao
    mensagem = 'Digite o segundo valor para a operação Matemática: \n'
    input_dois = recebe_numero(mensagem)
    if input_dois == 'exit':
        return input_um, input_dois, operacao
    
    return input_um, input_dois, operacao
    