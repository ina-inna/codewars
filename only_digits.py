def filter_string(st):
    new_st = ''.join([char for char in st if char.isdigit()])
    return int(new_st)