def likes(names):
    n = len(names)
    if n >= 4:
        statement = f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    elif n == 1:
        statement = f"{names[0]} likes this"
    elif n == 2:
        statement = f"{names[0]} and {names[1]} like this"
    elif n == 3:
        statement = f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        statement = "no one likes this"
        
    return statement
