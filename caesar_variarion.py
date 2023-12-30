def moving_shift(s, shift):
    new_s = ''
    for char in s:
        if ord(char) >= 65 and  ord(char) <= 90:
            number1 = (ord(char) - ord('A') + shift) % 26 + ord('A')
            char = chr(number1)
            new_s += char
            shift += 1
        elif ord(char) >= 97 and  ord(char) <= 122:
            number2 = (ord(char) - ord('a') + shift) % 26 + ord('a')
            char = chr(number2)
            new_s += char
            shift += 1
        else:
            new_s += char
            shift += 1
    if len(new_s) % 5 == 0:
        target_length = len(new_s)//5
    else:
        target_length = (len(new_s)//5)+1
    result = []
    for i in range(4):
        a = i*target_length
        b = a + target_length
        result.append(new_s[a:b])
    result.append(new_s[b:])
    return result



def demoving_shift(s, shift):
    new_s = ''.join(s)
    decoded = ''
    for char in new_s:
        if ord(char) >= 65 and  ord(char) <= 90:
            number1 = (ord(char) - ord('A') - shift) % 26 + ord('A')
            char = chr(number1)
            decoded += char
            shift += 1
        elif ord(char) >= 97 and  ord(char) <= 122:
            number2 = (ord(char) - ord('a') - shift) % 26 + ord('a')
            char = chr(number2)
            decoded += char
            shift += 1
        else:
            decoded += char
            shift += 1
            
    return decoded