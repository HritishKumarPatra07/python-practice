"""WAY 1 - WHILE LOOP """

num = int(input('Enter Your Number : '))
tem = num
count_of_digit = 0

while (tem > 0):
    digit = tem % 10
    count_of_digit = count_of_digit + 1
    tem = tem // 10
print(f"{num} : Count Of Digit Value Is : {count_of_digit}")    

"""WAY 2 - FUNCTIONS """ 

def count_digit(num):
    tem = num
    count_of_digit = 0

    while( tem > 0):
        digit = tem % 10
        count_of_digit = count_of_digit + 1
        tem = tem // 10
    return f"{num} : Count Of Digit Value Is : {count_of_digit}"

print(count_digit(2456))
print(count_digit(245556))
print(count_digit(24356))
print(count_digit(56))
