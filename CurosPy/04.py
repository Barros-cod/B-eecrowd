"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""

# name = 'Barros'
# price = 10000.39423223
# variable = '%s, The total price was R$%.2f' % (name, price)
# variable = '%s, The total price was R$%.2f hex %05x' % (name, price, 10000)
# print(variable)
# print('O hexadecimal de %d é %04x' % (1500, 1500))
# print('O hexadecimal de %d é %08X' % (15000, 15000))


"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
# variavel = 'ABC'
# print(f'{variavel}')
# print(f'{variavel: >10}')
# print(f'{variavel: <10}.')
# print(f'{variavel: ^10}.')
# print(f'{1000.4873648123746:0=+10,.1f}')
# print(f'O hexadecimal de 1500 é {1500:08X}')
# print(f'{variavel!r}')

"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

# variavel = 'Olá mundo'
# print(variavel[4:])
# print(variavel[4:7])
# print(variavel[0:9:2])
# print(variavel[:4])
# print(variavel[::-1])
# print(variavel[-1:-10:-1])
# print('São', len(variavel),'Caracteres')

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÂO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')  
else:
    print('Desculpe, você deixou campos vazios.')