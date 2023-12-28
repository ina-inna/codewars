def beeramid(bonus, price):
    i = 1
    if bonus - (i**2)*price < 0:
        return 0
    else:
        while bonus - (i**2)*price >= 0:
            bonus = bonus - (i**2)*price
            if bonus - ((i+1)**2)*price < 0:
                return i
            else:
                i +=1
        return i