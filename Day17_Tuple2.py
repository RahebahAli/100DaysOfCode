Number = (4, 6, 7, 3, 1, 3, 5, 9, 0, 6)
print(Number)
# Check if Item Exists.
if 2 in Number:
	print("Yes")
else:
	print("No")

if 3 in Number:
	print("Yes")
else:
	print("No")
#Repeat Item in Tuple.
Repeat = (3,) * 4
print(Repeat)
# Merge two tuples.
Number = Number + Repeat
print(Number)
# To calculates the number of items a tuple.
print(len(Number))
# Convert from list to tuple.
FruitsList = ["Apple", "banana", "orange", "Strawberries"]
FruitsTuple = tuple(FruitsList)
print(FruitsTuple)
# display from index 2 to the end.
print(FruitsTuple[2:])
#To place a specific text between each of the two elements
for i in range(5):
	s = '-'.join(FruitsTuple)
print(s)
''' To calculates the maximum, the minimum,
index for specified item and count for specified item.'''
print(max(Number))
print(min(Number))
print(Number.count(3))
print(Number.index(7))