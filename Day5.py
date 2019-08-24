#Assign a value to the variables
a = "Apple "
b = "Orange "
c = "Limon "

#Combine values ​​with one variable and display
basket = a + b + c
print(basket)

#The first way by using len() and display
n = 6
print([basket[i:i+n] for i in range(0, len(basket), n)])

#The second way by using split() and display
x = basket.split()
print(x)