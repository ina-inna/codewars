def pig_it(text):
    words = text.split()
    modified_words = [word + word[0] + 'ay' for word in words]
    modified_words = [word.replace(word[0], '', 1) for word in modified_words]
    text_final= ' '.join(modified_words)
    if '?' in text_final:
        split = text_final.split('?')
        return split[0] + '?'
    if '!' in text_final:
        split = text_final.split('!')
        return split[0] + '!'
    else:
        return text_final