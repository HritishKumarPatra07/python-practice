"""WAY 1 - FOR LOOP """

num = int(input('Enter Your Number : '))

Square = []
Cube = []

for i in range(1 , num +1):
    Square.append(i ** 2) 
    Cube.append(i ** 3) 

print(f"Square Value Is  : {Square}")
print(f"Cube Value Is : {Cube}")  


"""WAY 2 - FUNCTIONS """

def Square_Cube(num):
     
    Square = []
    Cube = []

    for i in range(1 , num+1):
        Square.append(i ** 2)
        Cube.append(i ** 3)

    print(f"Square Value Is  : {Square}")
    print(f"Cube Value Is : {Cube}")  

Square_Cube(5)    
