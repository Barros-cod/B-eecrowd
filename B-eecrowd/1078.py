"""
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N

Entrada
A entrada contém um valor inteiro N (2 < N < 1000).

Saída
Imprima a tabuada de N, conforme o exemplo fornecido.
"""
valor_entrada = int(input())
i = 0
for i in range(10):
    i += 1
    soma = i * valor_entrada
    print(f'{i} x {valor_entrada} = {soma}')
