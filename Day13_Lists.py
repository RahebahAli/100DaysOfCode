# Create a List
new_List = []
# String list
Fruits = ["apple", "banana", "orange"]
# Number list
integer_Numbers = [1, 2, 3, 4, 5, 6]
float_Numbers = [4.6, 7.9, 4.2, 1.2]
print(new_List) # []

# Merge two lists
Merge_Lists = Fruits + integer_Numbers
print(Merge_Lists) # ['apple', 'banana', 'orange', 1, 2, 3, 4, 5, 6]

# Access Items 
print(integer_Numbers[3]) # 4
print(float_Numbers) # [4.6, 7.9, 4.2, 1.2]
print(Fruits[-1]) # orange

#  Loop Through a List 
for x in integer_Numbers:
	print(x)

# Change item value
Fruits[2] = "Grape"
print(Fruits) # ['apple', 'banana', 'Grape']

# Removes the specified index
del integer_Numbers[3]
print(integer_Numbers) # [1, 2, 3, 5, 6]

# Delete the list completely
del Merge_Lists
print(Merge_Lists) # name 'Merge_Lists' is not defined