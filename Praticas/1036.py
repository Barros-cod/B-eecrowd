'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Exemplos de Entrada:
10.0 20.1 5.1

0.0 20.0 5.0

10.3 203.0 5.0

10.0 3.0 5.0
'''
import math

valor = input().split()

a = float(valor[0])
b = float(valor[1]) 
c = float(valor[2])

delta = (b ** 2) - 4 * a * c


if delta < 0:
    print("Impossivel calcular")
elif a == 0:
    print("Impossivel calcular") 
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print(f"R1 = {x1:.5f}\nR2 = {x2:2.5f}")


