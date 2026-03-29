"""WAY 1 - WHILE LOOP """

num = int(input('Enter Your Number : '))
tem = num
smallest_digit = tem % 10

while(tem > 0):
    digit = tem % 10
    if digit < smallest_digit:
        smallest_digit = digit
    tem = tem // 10

print(f"{num} : Smallest Of Digit Is : {smallest_digit} ") 

"""WAY 2 - FUNCTIONS """ 

def smallest_digit(num):
    tem = num
    smallest_of_digit = tem % 10

    while(tem > 0):
        digit = tem % 10
        if digit < smallest_of_digit:
            smallest_of_digit = digit
        tem = tem // 10

    return f"{num} : Smallest Digit Is : {smallest_of_digit}"

print(smallest_digit(2134567)) 
print(smallest_digit(567))
print(smallest_digit(3257))    
            