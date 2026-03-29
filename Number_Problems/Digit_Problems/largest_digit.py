"""WAY 1 - WHILE LOOP """

num = int(input('Enter Your Number : '))
tem = num
largest_digit = 0

while(tem > 0):
    
    digit = tem % 10
    
    if digit > largest_digit:
            largest_digit = digit
    tem = tem // 10
print(f"{num} : Largest Of Digit Is : {largest_digit} ")    


"""WAY 2 - FUNCTIONS """ 

def largest_digit(num):
    tem = num 
    largest_of_digit = 0

    while(tem > 0):
        digit = tem % 10
        if digit > largest_of_digit:
            largest_of_digit = digit
        tem = tem // 10
    return f"{num} : Largest Digit Is : {largest_of_digit}"
print(largest_digit(3245654))       
print(largest_digit(85654))  
print(largest_digit(324569))  