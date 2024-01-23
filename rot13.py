def rot13(message):
    new_s = ''
    for char in message:
        if ord(char) >= 65 and  ord(char) <= 90:
            number1 = (ord(char) - ord('A') + 13) % 26 + ord('A')
            char = chr(number1)
            new_s += char
        elif ord(char) >= 97 and  ord(char) <= 122:
            number2 = (ord(char) - ord('a') + 13) % 26 + ord('a')
            char = chr(number2)
            new_s += char
        else:
            new_s += char
    return new_s