"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
"""

valores = []

for i in range(5):
    valores.append(int(input()))

pares = [valor for valor in valores if valor % 2 == 0]

quantidade_pares = len(pares)

print(f'{quantidade_pares} valores pares')
