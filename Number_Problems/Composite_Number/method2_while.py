num = int(input('Enter Your Number : '))
count = 0
start_point = 1
while ( start_point <= num):
    if num % start_point == 0 :
        count = count + 1
    start_point = start_point + 1

if count > 2 :
    print(f"{num} : Is Composite")
else:
    print(f"{num} : Is Not Composite")   

