import random

x = 1      #Int
y = 2.3    #Float
z = 45e6   #Float
p = 7+8j   #Complex

print(type(x))
print(type(y))
print(type(z))
print(type(p))

#To convert from one type to another :

a = float(x)
b = int(y)
c = complex(z)

#To display the value
print(a)
print(b)
print(c)

#To display the type
print(type(a))
print(type(b))
print(type(c))

#To display a random number between 1 and 99
print(random.randrange(1,100))