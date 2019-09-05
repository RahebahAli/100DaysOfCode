# Create a tuple
Number = () # Empty
print(Number)
Number2 = (5,) # One item
print(Number2)
Number3 = (4, 7, 8, 2, 9, 2, 0) # Multiple items
print(Number3)

for x in Number3:
	print(x)

# Can not change values, add item and remove item in tuple.
Number3[3] = 5

Number3.append(6)

del Number3[1]

print(Number3)

# To delete all the tuple
del Number2
print(Number2)