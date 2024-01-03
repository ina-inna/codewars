def gimme_the_letters(sp):
    new_sp = ""
    ascii1 = ord(sp[0])
    ascii2 = ord(sp[2])+1
    for i in range (ascii1, ascii2, 1):
        new_sp += chr(i)
    return new_sp