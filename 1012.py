inputs = input().split()
a, b, c = map(float, inputs)

triangle = (a * c) / 2
circle = 3.14159 * c**2
trapezium = ((a+b) * c) / 2
square = b**2
rectangle = a*b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
