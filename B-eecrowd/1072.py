"""Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo."""

n = int(input())
in_ = 0
out = 0

for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        in_ += 1
    else:
        out += 1
    
print(f'{in_} in')
print(f'{out} out')
