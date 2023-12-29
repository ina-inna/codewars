def duplicate_encode(word):
    char_counts = {}
    word = word.lower()
    for char in word:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    new_string = ""
    for char in word:
        if char_counts[char] > 1:
            new_string += ")"
        else:
            new_string += "("
            
    return new_string