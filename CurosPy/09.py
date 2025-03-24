#  Introdução às Generator functions em Python 3 
#  yield from em generator functions
    # def generator(n=0, maximum=10):
    #     while True:
    #         yield n
    #         n += 1
    #         if n > maximum:
    #             return


        # yield 1  yield é uma palavra reservada que retorna um valor e pausa a execução da função
        # print('Estou no meio da função')
        # yield 2
        # print('Mais uma vez')
        # yield 3
        # print('Fim da função')
        # return 

    # gen = generator()
    # print(gen.__iter__())
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

    # for i in gen:
    #     print(i)

    # def gen1():
    #     yield 1
    #     yield 2
    #     yield 3

    # def gen2(gen):
    #     yield from gen()
    #     yield 4
    #     yield 5
    #     yield 6

    # g = gen2(gen1)
    # for i in g:
    #     print(i)

# try e except para tratar exceções
# try precisa de outro bloco para funcionar, o except
    # try:
    #     a = 18
    #     b = 0
    #     # print(b[0])
    #     # print('linhab'[110])
    #     c = a / b
    # except Exception as e: # Exception é a classe base para todas as exceções
    #     print(f'Erro: {e}')
    #     print(f'Nome: {e.__class__.__name__}')
        

    # print('Fim do programa')

    # try:
    #     print('Abri o arquivo')
    #     8/0 # ZeroDivisionError
    # except ZeroDivisionError as e:
    #     print(f'Erro: {e.__class__.__name__}')
    #     print(e)
    #     print('Divisão por zero')
    # except FileNotFoundError as e:
    #     print(f'Erro: {e.__class__.__name__}')
    #     print(e)
    #     print('Arquivo não encontrado')
    # except Exception as e:
    #     print(f'Erro: {e.__class__.__name__}')
    #     print(e)
    #     print('Erro desconhecido')
    # else:
    #     print('Não houve exceção')
    # finally:
    #     print('Fecha o arquivo')