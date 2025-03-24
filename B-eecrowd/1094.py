"""
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
"""

quantidade_testes = int(input())
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for _ in range(quantidade_testes):
    try:
        quantidade, tipo = input().split()
        quantidade = int(quantidade)
        if tipo == 'C':
            total_coelhos += quantidade
        elif tipo == 'R':
            total_ratos += quantidade
        elif tipo == 'S':
            total_sapos += quantidade
        else:
            continue  # Ignora tipos inválidos
    except ValueError:
        print('Digite um número inteiro para a quantidade.')
        exit()
    except:
        print('Entrada inválida.')
        exit()

total = total_coelhos + total_ratos + total_sapos
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')

if total > 0:
    print(f'Percentual de coelhos: {total_coelhos / total * 100:.2f} %')
    print(f'Percentual de ratos: {total_ratos / total * 100:.2f} %')
    print(f'Percentual de sapos: {total_sapos / total * 100:.2f} %')
else:
    print('Não houve experimentos')