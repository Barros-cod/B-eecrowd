"""Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares."""
valor = int(input())
contador = 0
numero = valor
while contador < 6:
    if numero % 2 != 0:
        print(numero)
        contador += 1
    numero += 1
    