#Empacotamento e desempacotamento de dicionários
    # a, b = 1, 2
    # a, b = b, a
    # print(a, b) 

    # (a1, a2),(b1, b2) = pessoa.items()
    # print(a1, a2)
    # print(b1, b2)

    # for chave, valor in pessoa.items():
    #     print(f'{chave}: {valor}')

    # pessoa = {
    #     'nome': 'Barros',
    #     'Sobrenome': 'Junior',
    # }

    # dados_pessoas = {
    #     'idade': 20,
    #     'altura': 1.80,
    # }

    # pessoa_completa = {**pessoa, **dados_pessoas}
    # print(pessoa_completa)
    # print(pessoa, dados_pessoas)

    # def mostra_dados(*args, **kwargs):
    #     print('NÂO NOMEADOS:', args)

        # print(kwargs)
        # for chave, valor in kwargs.items():
        #     print(f'{chave}: {valor}')

    # mostra_dados(1, 2,nome='cleito', qlq=123)
    # mostra_dados(**pessoa_completa)

    # configuracoes = {
    #     'arg1': 1,
    #     'arg2': 2,
    #     'arg3': 3,
    #     'arg4': 4,
    # }

    # mostra_dados(**configuracoes)

    #LIST COMPREHENSION

    # print(list(range(10)))


    # lista = []
    # for i in range(10):
    #     lista.append(i)
    # print(lista)

    # lista = [
    #     i * 2
    #     for i in range(10)
    # ]
    # print(lista)

# Mapeamento de dados em list comprehension
    # import pprint

    # def p(v):
    #     pprint.pprint(v, sort_dicts=False, width=40)

    # produtos = [
    #     {'nome': 'p1', 'preco': 13},
    #     {'nome': 'p2', 'preco': 55},
    #     {'nome': 'p3', 'preco': 5},
    # ]

    # print(novo_produto)
    # print(*novo_produto, sep='\n')
    # p(novo_produto)
    # lista = [n for n in range(10) if n < 6]
    # print(lista)

    # novo_produto = [
    #     # produto['nome']
    #     # {'nome': produto['nome'], 'preco': produto['preco'] * 1.05}
    #     {**produto, 'preco': produto['preco'] * 1.05}
    #     if produto['preco'] > 20 else {**produto}
    #     for produto in produtos
    #     if ( produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
    # ]
    # p(novo_produto)

#Exercício Básico: Processamento de Dados de Alunos

# alunos = [
#     {'nome': 'Ana', 'nota': 8.5},
#     {'nome': 'Pedro', 'nota': 6.0},
#     {'nome': 'Maria', 'nota': 9.2},
#     {'nome': 'João', 'nota': 5.5},
#     {'nome': 'Carla', 'nota': 7.8},
# ]

# for aluno in alunos:
#     if aluno['nota'] >= 7:
#         print(f'{aluno["nome"]} Você foi Aprovado')
#     else:
#         print(f'{aluno["nome"]} Você foi Reprovado')
        
# nomes_aprovados = [aluno['nome'] for aluno in alunos if aluno['nota'] >= 7.0]
# print("\nNomes dos alunos aprovados:", nomes_aprovados)
# nomes_aprovados = [aluno['nome'] for aluno in alunos if aluno['nota'] <= 7.0]
# print("\nNomes dos alunos reprovados:", nomes_aprovados)
