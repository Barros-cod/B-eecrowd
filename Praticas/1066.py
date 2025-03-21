"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
"""

valores = []

for i in range(5):
    valores.append(int(input()))

pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]
positivos = [valor for valor in valores if valor > 0]
negativos = [valor for valor in valores if valor < 0]

print(f'{len(pares)} valor(es) par(es)')
print(f'{len(impares)} valor(es) impar(es)')
print(f'{len(positivos)} valor(es) positivo(s)')
print(f'{len(negativos)} valor(es) negativo(s)')