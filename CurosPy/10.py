# raise - lançando exceções (erros)
    # print(123)
    # raise ValueError('Deu erro')
    # print(432)
    # def nao_aceito_zero(d):
    #        if d == 0:
    #         raise ZeroDivisionError(f'Vocé está tentando dividir por {d}')
    #        return True

    # def deve_ser_int_ou_float(n):
    #     tipo_n = type(n)
    #     if not isinstance(n, (float, int)):
    #         raise TypeError(
    #             f'"{n}" deve ser int ou float'
    #             f'"{tipo_n.__name__}" Enviado'
    #         )
    #     return True

    # def divide(n, d):
        # try:
        #     return n / d
        # except ZeroDivisionError:
        #     print('---------')
        #     raise
    #     deve_ser_int_ou_float(n)
    #     deve_ser_int_ou_float(d)
    #     nao_aceito_zero(d)
    #     return n / d
    # print(divide(8, '0'))

#Módulos padrão do Python (import, form, as e *)
    # import sys
    # print(sys.platform)

    # from sys import exit, platform
    # print(platform)

    # import sys as s "as" - apelido
    # sys = 'alguma'
    # print(sys)
    # print(s.platform)

    # from sys import exit as ex
    # from sys import platform as pf

    # print(pf)
    # print(ex)

    # má pratica - from nome_modulo import *
    # vantagens: importa tudo de um módulo
    # desvantagens: importa tudo de um módulo
    # from sys import *

    # print(platform)
    # exit()

# Modularização - Entendendo os seus próprios módulos e sys.path no Python
# try:
#     import sys
#     sys.path.append('C:/Users/Barros/')
# except ModuleNotFoundError:
#     ...
# import xps

# print('Módulo',__name__)
# print(*sys.path, sep='\n')

# import xps - crie um modulo
# from xps import soma

# print('Este módulo se chama', __name__)
# print(xps.variavel_modulo)
# n = int(input('Digite um valor: '))
# b = int(input('Digite um valor: '))

# print(soma(n, b))