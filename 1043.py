def valida_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False

x, y, z = map(float, input().split())

if valida_triangulo(x, y, z):
    print(f"Perimetro = {x + y + z:.1f}")
else:
    print(f"Area = {((x + y) * z) / 2:.1f}")
    