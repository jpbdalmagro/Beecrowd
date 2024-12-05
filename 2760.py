frase1 = list(input())
frase2 = list(input())
frase3 = list(input())

print(f"{''.join(frase1)}{''.join(frase2)}{''.join(frase3)}")
print(f"{''.join(frase2)}{''.join(frase3)}{''.join(frase1)}")
print(f"{''.join(frase3)}{''.join(frase1)}{''.join(frase2)}")
print(f"{''.join(frase1[:10])}{''.join(frase2[:10])}{''.join(frase3[:10])}")
