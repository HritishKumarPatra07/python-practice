"""WAY 1 - WHILE LOOP """

num = int(input('Enter Your Number : '))
tem = num
product_of_digit = 1

while(tem > 0):
    digit = tem % 10
    product_of_digit = product_of_digit * digit
    tem = tem // 10
print(f"{num} : Product Of Digit Value Is : {product_of_digit}")    



"""WAY 2 - FUNCTIONS """ 

def product_of_digit(num):
    tem = num 
    product_of_digits = 1

    while(tem > 0):
        digit = tem % 10
        product_of_digits = product_of_digits * digit
        tem = tem // 10

    return f"{num} : Product Of Digit Value Is : {product_of_digits}"    

print(product_of_digit(245))
print(product_of_digit(45))
