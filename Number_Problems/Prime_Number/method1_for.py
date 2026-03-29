num = int(input('Enter Your Number : '))

for i  in range(2 , num // 2):
    if num % i == 0 :
        print(f"{num} : Is Not Prime")
        break
else:
    print(f"{num} : Is Prime")