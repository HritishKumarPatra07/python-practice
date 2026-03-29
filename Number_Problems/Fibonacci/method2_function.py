def fibonacci_series(num):
    a = 0
    b = 1

    while(a <=num):

      print( f"{a}" , end =" ")
      tem = a + b
      a = b
      b = tem
  
fibonacci_series(19) 