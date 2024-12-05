def decimal_para_hexadecimal(numero):
    return hex(numero)

numero_decimal = int(input())
hexadecimal = decimal_para_hexadecimal(numero_decimal)
print(hexadecimal[2:].upper())
