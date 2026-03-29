def pos_neg(num):
    if num >= 0:
        print(num,': IS POSITIVE')
    else:
        print(num,': IS NEGATIVE')    
pos_neg(-55)   

def pos_neg(num):
    return f"{num} : IS POSITIVE" if num >=0 else f"{num} : IS NEGATIVE"

print(pos_neg(-55))