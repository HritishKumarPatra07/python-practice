num = int(input('Enter Your Number : '))
count = 0
for i in range(1,num+1):
    if num % i == 0 :
        count = count + 1

if count > 2 :
    print(f"{num} : Is Composite")
else:
    print(f"{num} : Is Not Composite")   
