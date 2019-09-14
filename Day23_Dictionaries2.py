Student = {'ID': 1102, 'Name': 'Ali', 'Level': 'Six'}

if "Level" in Student: # YES
	print("YES")
else:
	print("NO")

print(len(Student)) # 3

Student["Age"] = 20
print(Student) #{'ID': 1102, 'Name': 'Ali', 'Level': 'Six', 'Age': 20}

Student.pop("Level")
print(Student) #  {'ID': 1102, 'Name': 'Ali', 'Age': 20}

Student.clear()
print(Student) # {}

del Student
print(Student) # Error