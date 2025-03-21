import math

precos = [4.00, 4.50, 5.00, 2.00, 1.50]
valor = input().split()

a = float(valor[0])
b = float(valor[1]) 

if a == 1:
    soma = b * 4.00
    print(f"Total: R$ {soma:.2f}")
elif a == 2:
    soma = b * 4.50
    print(f"Total: R$ {soma:.2f}")
elif a == 3:
    soma = b * 5
    print(f"Total: R$ {soma:.2f}")
elif a == 4:
    soma = b * 2.00
    print(f"Total: R$ {soma:.2f}")
elif a == 5:
    soma = b * 1.50
    print(f"Total: R$ {soma:.2f}")
