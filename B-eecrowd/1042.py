'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

7 21 -14

-14 21 7
'''
import math
valores = input().split()
a, b, c = int(valores[0]), int(valores[1]), int(valores[2])

original = [a, b, c]

ordenados = sorted(original)

for valor in ordenados:
    print(valor)

print()
for valor in original:
    print(valor)