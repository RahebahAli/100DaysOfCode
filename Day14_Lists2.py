# Split lists
Fruits = ["apple", "banana", "orange", "Grape", "Strawberries"]
print(Fruits[1:4]) #['banana', 'orange', 'Grape']

# Check if Item Exists
if "Strawberries" in Fruits: # Yes
	print("Yes")
else:
	print("No")

if "Pineapple" in Fruits: # No
	print("Yes")
else:
	print("No")

#Repeat Item in List
integer_Numbers = [5] * 3
print(integer_Numbers) #[5, 5, 5]

# Merge two lists
float_Numbers = [7.08, 1.59, 4.11, 74.8]
Numbers = float_Numbers + integer_Numbers
print(Numbers) #[4.6, 7.9, 4.2, 1.2, 5, 5, 5]