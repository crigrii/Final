def representacion_ascii(byte):
    valor_decimal = int(byte, 2)
    caracter_ascii = chr(valor_decimal)
    return caracter_ascii, valor_decimal

byte_binario = input("Ingrese el byte en formato binario: ")

caracter_ascii, valor_decimal = representacion_ascii(byte_binario)

print(f"La representación ASCII del byte '{byte_binario}' es: {caracter_ascii}-{valor_decimal}")
