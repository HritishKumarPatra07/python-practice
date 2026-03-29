num = int(input('Enter Your Number : '))
tem = num
sum_of_digit = 0

for i in range(1,tem):
    if  tem % i == 0:
        sum_of_digit = sum_of_digit + i
if num == sum_of_digit :
    print(f"{num} : Is Perfect : {sum_of_digit}")
else:
    print(f"{num} : Is Not Perfect : {sum_of_digit}")      
