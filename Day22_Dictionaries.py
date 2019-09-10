# In Python dictionaries are written with curly brackets {}
Student = {"ID":1102, "Name":"Ali"}# Create a dictionary
print(Student)

Student["Level"] = "Five" # Add an item
print(Student)

for x in Student:
	print(Student[x]) # Display just a values

for x in Student.values():
	print(x) # Display just a values

for x, y in Student.items():
	print(x, y) # Display the values and the keys 

print(Student.items()) # Display the values and the keys 

Student["Level"] = "Six" # Change an item
print(Student)