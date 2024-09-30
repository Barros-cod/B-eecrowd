p1 = input().split()

a = int(p1[0])
b = int(p1[1])
c = int(p1[2])
d = int(p1[3])

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

