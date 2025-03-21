"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada	Exemplos de Saída
vertebrado
mamifero
onivoro

homem

vertebrado
ave
carnivoro

aguia

invertebrado
anelideo
onivoro

minhoca
"""
animais = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
         'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
          'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

primeiro_nome = input()
segundo_nome = input()
terceiro_nome = input()

if primeiro_nome in animais and \
    segundo_nome in animais[primeiro_nome] and \
    terceiro_nome in animais[primeiro_nome][segundo_nome]:
    print(animais[primeiro_nome][segundo_nome][terceiro_nome])