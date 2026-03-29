"""WAY- 1 """
a = 10
b = 20 

a = a + b

b = a - b
a = a - b

print(f"A : {a}")
print(f"B : {b}")

"""WAY- 2 """

a = 30
b = 40 

a,b = b,a

print(f"A : {a}")
print(f"B : {b}")

"""WAY- 3 """

a = 50
b = 60

c = a
a = b
b = c

print(f"A : {a}")
print(f"B : {b}")

"""WAY- 4  """

a = 70
b = 80

c = a + b

b = c - b
a = c - b

print(f"A : {a}")
print(f"B : {b}")