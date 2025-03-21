"""Receber dois números.
Descobrir qual é o menor e qual é o maior.
Olhar para cada número que está no meio deles.
Verificar se esse número é ímpar.
Se for ímpar, vai guardar esse número para somar depois.
No final, vai mostrar a soma de todos os números ímpares que encontrou."""

x = int(input())
y = int(input())

if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x

soma = 0
for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma += i

print(soma)