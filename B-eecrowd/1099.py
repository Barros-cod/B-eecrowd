def soma_impares(x, y):
    soma = 0
    if x > y:
        x, y = y, x
    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i
    return soma

n = int(input())
for _ in range(n):
    linha = input().split()
    x = int(linha[0])
    y = int(linha[1])
    resultado = soma_impares(x, y)
    print(resultado)
