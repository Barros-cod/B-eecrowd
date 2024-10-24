''' 
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

4.5 -2.2

0.1 0.1
0.1 0.1

0.0 0.0

'''
import math

valores = input().split()

x, y = float(valores[0]),float(valores[1])

if x == 0 and y == 0:
    print("Origem")
elif y == 0:
    print("Eixo X")
elif x == 0:
    print("Eixo Y")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")
