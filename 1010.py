p1 = input().split()
p2 = input().split()
valor = int(p1[0])
valor2 = float(p1[1])
valor3 = float(p1[2])

valor1 = int(p2[0])
valor4 = float(p2[1])
valor5 = float(p2[2])

valor_total = (valor3 * valor2) + (valor4 * valor5)

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")



