""" 
Introdução ao try / exxept
try > Tentar executar o código
except > Ocorreu algum erro ao tentar executar

"""

    # ValueError: Ocorre quando uma operação é realizada com um valor de tipo incorreto.
    # TypeError: Ocorre quando uma operação é realizada com tipos de dados incompatíveis.
    # IndexError: Ocorre quando você tenta acessar um elemento de uma lista ou tupla que não existe.
    # KeyError: Ocorre quando você tenta acessar uma chave que não existe em um dicionário.


    # numb_str = input('Vou dobra o número: ')
    # if numb_str.isdigit(): # verifica se uma string representa um número inteiro.
    #     numb_float = float(numb_str) 
    #     print(f'O dobro de {numb_str} é {numb_float * 2:.2f}')
    # else:
    #     print('Isso não é um número')
    # numb_str = input('Vou dobra o número: ')

    # try:
    #     numb_float = float(numb_str) 
    #     print('FLOAT', numb_float)
    #     print(f'O dobro de {numb_str} é {numb_float * 2:.2f}')
    # except:
    #     print('Isso não é um número')


"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
            <- Contagem de complexidade (ruim)
"""

    # velocidade = 61 # Velocidade atual do Carro
    # local_carro = 101 #Local em que o carro esta na estrada


    # RADAR_1 = 60  # velocidade máxima do radar 1
    # LOCAL_1 = 100  # local onde o radar 1 está
    # RADAR_RANGE = 1  # A distância onde o radar pega


    # velocidade_carro_passo_radar_1 = velocidade > RADAR_1
    # carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_carro_passo_radar_1
    # carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passo_radar_1

    # if velocidade_carro_passo_radar_1:

    #     print('Velocidade carro passou do rada 1')

    # if carro_passou_radar_1:
    #     print('Carro passou rada 1')

    # if carro_passou_radar_1:

    #     print('Multado')


""" 
Flag (Bandeira) - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identindade
"""
    # v1 = 'a'
    # v2 = 'b'
    # print(id(v1))
    # print(id(v2))

    # condicao = False
    # passou_no_if = None

    # if condicao:
    #     passou_no_if = True # < Criar variaveis dentro de um if pode gerar erros.
    #     print('Faça algo')
    # else:
    #     print('Não faça algo')

    # if passou_no_if is None:
    #     print('Não passou no if')

    # if passou_no_if is not None:
    #     print('Passou no if')

    # print(passou_no_if, passou_no_if is None)
    # print(passou_no_if, passou_no_if is not None)
    # print(id(passou_no_if))


"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_str = input('Digite um numero inteiro: ')
# try:
#     numero_inteiro = int(numero_str)
#     if numero_inteiro % 2 == 0:
#         print(f"O número {numero_inteiro} é par.")
#     else:
#         print(f"O número {numero_inteiro} é ímpar.")
# except ValueError:
#     print(f"Você não digitou um número inteiro válido.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horas = int(input('Que horas são agora: '))

# if horas >= 0 and horas <= 11:
#     print('Bom dia!')
# elif horas >= 12 and horas <= 17:
#     print('Boa tarde!')
# elif horas >= 18 and horas <= 23:
#     print('Boa noite!')
# else:
#     print('Horário inválido.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')