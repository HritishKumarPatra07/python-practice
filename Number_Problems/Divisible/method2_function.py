def divisible(num):
     if num % 3 == 0 and num % 5 == 0:
          return f"{num} : Is Divisible By 3 And 5 "
     else:
          return f"{num} : Is Not Divisible By 3 And 5 "
     
print(divisible(30))  
print(divisible(35))     
print(divisible(15))  