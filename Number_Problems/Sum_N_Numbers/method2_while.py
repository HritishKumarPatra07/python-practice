num = int(input('Enter Your Number :'))
start_num = 1
sum_of_digit = 0

while(start_num < num +1):
    sum_of_digit = sum_of_digit + start_num

    start_num = start_num + 1

print(num,': SUM OF DIGIT IS :',sum_of_digit)       
