num = int(input('Enter Your Number : '))
tem = num
sum_of_digit = 0
startpoint = 1

while (startpoint < tem):
    if tem % startpoint == 0 :
        sum_of_digit = sum_of_digit + startpoint

    startpoint = startpoint + 1

if num == sum_of_digit :
    print(f"{num} : Is Perfect : {sum_of_digit}")
else:
    print(f"{num} : Is Not Perfect : {sum_of_digit}") 