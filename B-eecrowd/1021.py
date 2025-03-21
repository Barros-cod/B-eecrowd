valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01 ]

print("NOTAS:")
for nota in notas:
    quantidade = valor // nota 
    valor = valor % nota 
    print(f"{quantidade:.0f} nota(s) de R$ {nota:.2f}")
print("MOEDAS:")
for moeda in moedas:
    valor = round(valor, 2)
    qt_moedas = int(valor / moeda)
    print(f"{qt_moedas:.0f} moeda(s) de R$ {moeda:.2f}")
    valor -= qt_moedas * moeda

