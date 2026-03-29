def fibonacci_series(num):
    a = 0
    b = 1
    result = []

    while(a <=num):
      result.append(a)
      tem = a + b
      a = b
      b = tem
    return result
  
print(fibonacci_series(19)) 