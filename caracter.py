def char_to_binary(char):
    if len(char) != 1:
        return "Por favor, ingrese solo un carácter."
    
    ascii_value = ord(char)
    
    binary_representation = format(ascii_value, '08b')
    
    return binary_representation

user_input = input("Ingrese un carácter: ")

binary_result = char_to_binary(user_input)
print(f"La representación binaria del carácter '{user_input}' es: {binary_result}")
