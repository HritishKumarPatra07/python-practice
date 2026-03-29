num = int(input('Enter Your Number :'))
tem = num  

StrongNum = 0

while (tem > 0):
    digit = tem % 10 

    factorial = 1
    for i in range (1 , digit +1):
        factorial = factorial * i

    StrongNum = factorial + StrongNum


    tem = tem // 10   

if num == StrongNum :
   print(f"{num} : Is Strong: {StrongNum}")
else:
  print(f"{num} : Is Not  Strong : {StrongNum}")
