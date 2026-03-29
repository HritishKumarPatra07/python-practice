def palindrome(num):
    tem = num
    reverse = 0
    while(tem > 0):
     digit = tem % 10
     reverse = reverse * 10 + digit
     tem = tem // 10

    if num == reverse :
       print(f"{num} : IS Palindrome : {reverse}")    
    else:
       print(f"{num} : Is Not Palindrome : {reverse}")  

palindrome(456)   
