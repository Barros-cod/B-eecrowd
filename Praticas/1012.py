p1 = input().split()

a = float(p1[0])
b = float(p1[1])
c = float(p1[2])

TRIANGULO = (a * c)/2
CIRCULO = 3.14159 * c**2
TRAPEZIO =  ((a + b) * c)/2
QUADRADO = b ** 2
RETANGULO = a * b

print(f"TRIANGULO: {TRIANGULO:.3f}")
print(f"CIRCULO: {CIRCULO:.3f}")
print(f"TRAPEZIO: {TRAPEZIO:.3f}")
print(f"QUADRADO: {QUADRADO:.3f}")
print(f"RETANGULO: {RETANGULO:.3f}")