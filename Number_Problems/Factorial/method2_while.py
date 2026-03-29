num = int(input('Enter Your Number :'))

startnum = 1
Factorial = 1

while (startnum <= num):

    Factorial = Factorial * startnum
    startnum = startnum + 1

print(f"{num} : Factorial Value Is : {Factorial} ")
