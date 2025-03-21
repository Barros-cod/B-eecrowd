    # lista = []
    # for x in range(3):
    #     for y in range(3):
    #         lista.append((x, y))

    # lista = [
    #     (x, y)
    #     for x in range(3)
    #     for y in range(3)
    # ]
    # lista = [
    #     [(x, letra) for letra in 'barros']
    #     for x in range(3)
    # ]

    # print(lista)

# Dict Comprehension e Set Comprehension
    # produtos = {
    #     'nome': 'Caneta Azul',
    #     'preco': 1.99,
    #     'categoria': 'Papelaria',
    # }

    # dc = {
    #     chave: valor.upper()
    #     if isinstance(valor, str) else valor
        # if isinstance(valor, (int, float)) else valor.upper()
    #     for chave, valor
    #     in produtos.items()
    #     if chave != 'categoria'
    # }

    # lista = {
    #     ('a', 'valor'),
    #     ('b', 'valor'),
    #     ('c', 'valor'),
    # }
    # print(dict(dc))

    # s1 = { 2 ** i for i in range(10)}
    # print(s1)
    # print(set(range(10)))

# isintance() - Verifica se o valor é do tipo especificado
# isinstance(valor, str) - Verifica se o valor é do tipo string
    # lista = [
    #     'a', 1, 1.2, True, 'b',{ 2, 2.3}, False, 'c', (3, 3.4),
    #     True, 4, 4.5, 'd', [5, 5.6]
    # ]

    # for item in lista:
    #     if isinstance(item, set):
    #         print('É um conjunto')
    #         item.add(5)
    #         print(item, isinstance(item, set))
    #     elif isinstance(item, str):
    #         print('É uma string')
    #         item = item + item
    #         item.upper()
    #         print(item.lower(), isinstance(item, str))
        
    #     elif isinstance(item, (int, float)):
    #         print('É um número')
    #         print(item, item * 2)
    #     else:
    #         print('Não sei o que é')
    #         print(item)

# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Truthy - Valores que são considerados verdadeiros em expressões booleanas
# Falsy - Valores que são considerados falsos em expressões booleanas
# Tipos Mutáveis - Listas, Dicionários e Conjuntos
# Tipos Imutáveis - Strings, Tuplas, Números e Booleanos
    # lista = []
    # dicioraio = {}
    # conjunto = set()
    # tupla = ()
    # string = ''
    # inteiro = 0
    # fluante = 0.0
    # nada = None
    # falso = False
    # intervalo = range(0)

    # def falsy(valor):
    #     return 'falsy' if not valor else 'truthy'

    # print(f'teste', falsy('teste'))
    # print(f'{lista=}', falsy(lista))
    # print(f'{dicioraio=}', falsy(dicioraio))
    # print(f'{conjunto=}', falsy(conjunto))
    # print(f'{tupla=}', falsy(tupla))
    # print(f'{string=}', falsy(string))
    # print(f'{inteiro=}', falsy(inteiro))
    # print(f'{fluante=}', falsy(fluante))
    # print(f'{nada=}', falsy(nada))
    # print(f'{falso=}', falsy(falso))
    # print(f'{intervalo=}', falsy(intervalo))

#dir, hasattr, getattr em python
    # string = 'barros'
    # metodo = 'lower'
    # # print(dir(string))
    # if hasattr(string, 'upper'):
    #     print(f'Tem o método {metodo}')
    #     print(getattr(string, metodo)())
    # else:
    #     print(f'Não tem o método {metodo}')

# Generator expression, Iterable e Iterator
# Generator expression - Gera valores sob demanda
# Iterable - Objeto que pode ser iterado
    # import sys

    # iterable = ['Barros', 'Python', 'Curso']
    # iterator = iter(iterable)
    # for valor in iterator:
    #     print(valor)
    # print(next(iterator)) 
    # generator = (n for n in range(100))
    # lista = [n for n in range(100)]
    # print(sys.getsizeof(lista))
    # print(sys.getsizeof(generator))

    # print(next(generator))
    # print(next(generator))
    # print(next(generator))

    # for n in generator:
    #     print(n)