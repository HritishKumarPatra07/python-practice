def composite_num(num):
    count = 0
    for i  in range (1 , num + 1):
        if num % i == 0 :
            count = count + 1

    if count > 2 :
      print(f"{num} : Is Composite")
    else:
       print(f"{num} : Is Not Composite")   

composite_num(5)       
composite_num(7)
composite_num(10)
composite_num(33)