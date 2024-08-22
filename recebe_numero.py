def recebe_numero(mensagem):
    input_var = input(f'{mensagem}')
    input_var = float(input_var) if input_var != 'exit' else input_var
    return input_var