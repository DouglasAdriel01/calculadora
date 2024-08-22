from operacoes import soma, subtrair, dividir, multiplicar, raizQuadrada, potencia

def selecionador_operacao(operacao):
    if operacao == '+':
        return soma
    elif operacao == '-':
            return subtrair
    elif operacao == '/':
            return dividir
    elif operacao == '*':
            return multiplicar
    elif operacao == 'v':
          return raizQuadrada
    elif operacao == '**':
          return potencia
    else:
        return 'Operação não permitida'