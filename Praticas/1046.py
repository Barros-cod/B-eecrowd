# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# Entrada
# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

# Saída
# Apresente a duração do jogo conforme exemplo abaixo.

# 16 2 O JOGO DUROU 10 HORA(S)
#  0 0 	O JOGO DUROU 24 HORA(S)
#  2 16 O JOGO DUROU 14 HORA(S)

tempo = input().split()

inicio,fim = int(tempo[0]), int(tempo[1])

if inicio < 0 or inicio > 23 or fim < 0 or fim > 23:
    print("Hora inválida")
else:
    # Calcular a duração
    if fim >= inicio:
        duracao = fim - inicio
    else:
        # Jogo passou da meia-noite
        duracao = 24 - inicio + fim

    # Verificar se a duração é válida (mínimo 1 hora, máximo 24 horas)
    if duracao < 1:
        duracao = 24

    print("O JOGO DUROU", duracao, "HORA(S)")