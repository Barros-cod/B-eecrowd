valor = int(input())

horas = valor // 3600
minutos = (valor % 3600) // 60
segundos = valor % 60

print(f"{horas}:{minutos}:{segundos}")