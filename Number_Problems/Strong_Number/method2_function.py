def strongnum(num):
    tem = num
    strong = 0

    while (tem > 0):
        digit = tem % 10
        factorial = 1

        for i in range(1,digit+1):
            factorial = factorial * i

        strong = strong + factorial

        tem = tem // 10
        
    if num == strong :
       print(f"{num} : Is Strong: {strong}")
    else:
         print(f"{num} : Is Not  Strong : {strong}")

strongnum(145)
