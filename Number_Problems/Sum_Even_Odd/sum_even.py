"""WAY 1 - FOR LOOP """

num = int(input('Enter Your Number : '))
sum_of_even = 0

for i in range(1,num+1):
    if i % 2 == 0:
        sum_of_even = sum_of_even + i
print(f"{num} : Sum Of Even Numbers Is : {sum_of_even}")        


"""WAY 2 - WHILE LOOP """


num = int(input('Enter Your Number : '))
sum_of_even = 0
start_point = 1
while(start_point <= num):
    if start_point  % 2 == 0:
        sum_of_even = sum_of_even + start_point

    start_point = start_point + 1      

print(f"{num} : Sum Of Even Numbers Is : {sum_of_even}")    



"""WAY 3 - FUNCTIONS """


def sum_of_even(num):
    sum_of_even_number = 0

    for i in range(1,num+1):
        if i % 2 == 0:
            sum_of_even_number = sum_of_even_number +  i

    return f"{num} : Sum Of Even Numbers Is : {sum_of_even_number}"  

print(sum_of_even(6)) 