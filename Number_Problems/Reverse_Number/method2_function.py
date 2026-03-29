def reverse(num):
    tem = num
    reverse_num = 0

    while(tem > 0):
        digit = tem % 10
        reverse_num = reverse_num * 10 +digit
        tem = tem // 10

    print(f"{num} : Reverse Number Is : {reverse_num}")    

reverse(3555)