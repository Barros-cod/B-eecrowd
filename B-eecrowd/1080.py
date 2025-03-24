"""Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo."""

valores = []

for i in range(5):
    try:
        valor = int(input())
        valores.append(valor)
    except ValueError:
        print('Digite um número inteiro')
        exit()
    
maior = valores[0]
posicao_maior = 1

for i in range(1, len(valores)):
    if valores[i] > maior:
        maior = valores[i]
        posicao_maior = i + 1

print(maior)
print(posicao_maior)