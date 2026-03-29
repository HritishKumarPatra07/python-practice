def fibonacci_series(num):
   if num == 0 :
      return 0
   elif num == 1:
      return 1
   else :
      return fibonacci_series(num-1) + fibonacci_series (num - 2)
   
print(fibonacci_series(10)) 