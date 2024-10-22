# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]Sair: ')
# senha = input('Senha: ')

# # if condicao quando for True: 
# if (entrada == 'E' or entrada == 'e') and senha == '12345':
#     print('Entrou no sistema')
# else:
#     print('Senha Errada.')


#Avaliação de curto circuito:
# print(True and True and True)
# print(True and False and True)
# print(True and 0 and True)
# print(True or False)
# print(0 or False or 0 or 'abc' or True)
# senha = input('Senha: ') or 'Sem senha'
# print(senha)

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
# if senha != '1234':
#     print('Senha incorreta.')

# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# # print(nome[2])
# # print(nome[-4])
# print('vio' in nome)
# print('z' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('z' not in nome)