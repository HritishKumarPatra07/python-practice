def Armstrong(num):
    tem = num
    digit_count = len(str(tem))
    sum_of_digit = 0
    while(tem > 0):
        digit = tem % 10 
        sum_of_digit = sum_of_digit + digit ** digit_count
        tem = tem // 10

    if num == sum_of_digit :
       print(f"{num} : Is Armstrong : {sum_of_digit}")
    else:
       print(f"{num} : Is Not  Armstrong : {sum_of_digit}")

Armstrong(153)
Armstrong(1634)