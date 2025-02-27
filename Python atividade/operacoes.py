def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero."
    elif a == 0:
        return "Erro: Não é possível dividir zero."
    return a / b