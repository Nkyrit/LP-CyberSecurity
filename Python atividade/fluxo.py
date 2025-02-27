valor = 100
matriz = [[valor - i for i in range(linha * 10, (linha + 1) * 10)] for linha in range(10)]
for linha in matriz:
    print(*linha)
