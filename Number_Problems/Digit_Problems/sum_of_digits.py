
"""WAY 1 - WHILE LOOP """

num = int(input('Enter Your Number : '))
tem = num
sum_of_digit = 0

while(tem > 0):
    digit = tem % 10
    sum_of_digit = sum_of_digit + digit
    tem = tem // 10
print(f"{num} : Sum Of Digit Value Is : {sum_of_digit}")    


"""WAY 2 - FUNCTIONS """ 

def sum_of_digit(num):
    tem = num
    sum_of_digits = 0

    while ( tem > 0):
        digit = tem % 10
        sum_of_digits = sum_of_digits + digit
        tem = tem // 10

    return f"{num} : Sum Of Digit Value Is : {sum_of_digits}"    

print(sum_of_digit(245))