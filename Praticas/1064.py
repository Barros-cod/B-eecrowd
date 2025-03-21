"""Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados."""

valores = []

for valor in range(6):
    valores.append(float(input()))

positivos = [valor for valor in valores if valor > 0]

quantidade_positivos = len(positivos)
media_positivos = sum(positivos) / quantidade_positivos if quantidade_positivos > 0 else 0

print(f'{quantidade_positivos} valores positivos')
print(f"{media_positivos:.1f}")