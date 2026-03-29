def prime_num(num):
    for i in range(2 , num // 2):
        if num % i == 0 :
           print(f"{num} : Is Not Prime")  
           break
    else:
      print(f"{num} : Is Prime")    
prime_num(2)   
prime_num(5)  
prime_num(7)     
prime_num(8)  
prime_num(10)  
prime_num(13)  