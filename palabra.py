def generar_representacion_en_bytes(palabra):
    bytes_list = []

    for char in palabra:
        byte_representation = bin(ord(char))[2:].zfill(8)  
        bytes_list.append(byte_representation)

    byte_string = ' '.join(bytes_list)

    return byte_string

palabra = input("Ingrese una palabra: ")

representacion_en_bytes = generar_representacion_en_bytes(palabra)

print("La representación en bytes de la palabra es:", representacion_en_bytes)
