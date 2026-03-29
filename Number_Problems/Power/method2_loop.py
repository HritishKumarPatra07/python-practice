num1 = int(input('Enter Your Number : '))
num2 = int(input('How Many Power : '))

power_value = 1
for i in range(1,num2+1):
    
    power_value = power_value * num1
print(power_value)    
