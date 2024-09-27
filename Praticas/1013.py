p1 = input().split()
a = int(p1[0])
b = int(p1[1])
c = int(p1[2])
maior = (a+b+abs(a-b))/2
maiorab = (c+maior+abs(c-maior))/2
print(f"{maiorab:.0f} eh o maior")
