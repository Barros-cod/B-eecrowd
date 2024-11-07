"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos: str, int, float, bool
"""

    # string = 'cleitinho Otávio'
    # outra_variavel = f'{string[:3]},ABC{string[4:]}'
    # print(string)
    # print(outra_variavel)
    # print(string.capitalize())
    # print(string.zfill(10))


"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
    # while (condição) {
    #     // Bloco de código a ser executado   
    #  enquanto a condição for verdadeira
    # }

    # while True:
    #     nome = input('Qual e seu nome: ')
    #     print(f'Seu nome é {nome}')
    #     print('Para sair do programa escreva "Sair"')

    #     if nome == 'Sair' and 'sair':
    #         break

    # print('Saiu do programa')

    # contador = 0

    # while contador <= 10: 
    #     print(contador)
    #     contador = contador + 1

    # print('Acabou')

    # contador = 0

    # while contador <= 100:
    #     contador += 1

    #     if contador == 6:
    #         print('Não vou mostrar', contador)
    #         continue
    #     if contador >= 10 and contador <= 27:
    #         print('Não vou mostrar', contador)
    #         continue
    #     print(contador)

    #     if contador == 40:
    #         break

    # print('Acabou')

    # quantas_linhas = 5
    # quantas_colunas = 5

    # linha = 1
    # while linha <= quantas_linhas:
    #     coluna = 1
    #     while coluna <= quantas_colunas:
    #         print(f'{linha=} {coluna=}')
    #         coluna += 1
    #     linha += 1

    # print('Acabou')
"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
    # contador = 5

    # contador += 1
    # print(contador)
    # contador *= 'test'
    # print(contador)

