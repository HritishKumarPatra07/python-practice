"""WAY 1 - FOR LOOP """

num = int(input('Enter Your Number : '))
sum_of_odd = 0

for i in range(1,num+1):
    if i % 2 != 0:
        sum_of_odd = sum_of_odd + i

print(f"{num} : Sum Of Odd Numbers Is : {sum_of_odd}")       


"""WAY 2 - WHILE LOOP """

num = int(input('Enter Your Number : '))
sum_of_odd = 0
start_point = 1

while(start_point <= num):
    if start_point % 2 != 0:
        sum_of_odd = sum_of_odd + start_point

    start_point = start_point + 1   

print(f"{num} : Sum Of Odd Numbers Is : {sum_of_odd}") 


"""WAY 3 - FUNCTIONS """

def sum_of_odd(num):
    sum_of_odd_number = 0

    for i in range(1,num + 1):
        if i % 2 != 0:
            sum_of_odd_number = sum_of_odd_number + i

    return (f"{num} : Sum Of Odd Numbers Is : {sum_of_odd_number}")       

print(sum_of_odd(6))