"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo."""

for i in range(1, 10, 2):
    for j in range(i + 6,i + 3, -1):
        print(f'I={i} J={j}')
    
        