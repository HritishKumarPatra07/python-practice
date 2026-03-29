num = int(input('Enter Your Number : '))
startpoint = 2

while(startpoint < num // 2):
    if num % startpoint == 0:
        print(f"{num} : Is Not Prime")
        break
    startpoint = startpoint + 1
else:
    print(f"{num} : Is Prime")
