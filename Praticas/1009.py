nome = input()

salario = float(input())
total = float(input())

comissao = total * 0.15

salario_total = salario + comissao 

print(f"TOTAL = R$ {salario_total:.2f}")