student = {"ID":"", "Name":"", "Level":""}

for x in student:
	if x == "ID":
		student[x] = int(input("Enter " + x +" : " ))
	else:
		student[x] = str(input("Enter " + x +" : " ))

print(student)