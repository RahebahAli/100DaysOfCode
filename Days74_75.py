import mysql.connector
'''file = open("python.txt", "x")

file = open("python.txt", "w")
file.write("""What is Python language?
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.
Its design philosophy emphasizes code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in language such as C++ or Java.
Python supports multiple programming paradigms, including object-oriented, imperative and
functional programming or procedural styles. It features a dynamic type system and automatic
memory management and has a large and comprehensive standard library""")
file.close()

# 1.1
file = open("python.txt", "r")
print(file.read())

# 1.2
file = open("python.txt", "a")
file.write("The best way we learn anything is by practice and exercise questions")
file.close()
file = open("python.txt", "r")
print(file.read())'''

# 2 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="myEmployee")# added (database="myEmployee") after created it

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE myEmployee")
#mycursor.execute("CREATE TABLE Employee(id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(10), LastName VARCHAR(10), Age INT, Gender VARCHAR(6), Salary INT)")
'''INS = "INSERT INTO Employee (FirstName, LastName, Age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
VAL = [
('Ahmed', 'Ali',30,'Male',10000),
('Khalid', 'Muhammad',34,'Male',7000),
('Norah', 'Saleh',29,'Female',7000) ]

mycursor.executemany(INS, VAL)
mydb.commit()'''

# 2.1
mycursor.execute("SELECT * FROM Employee")
for x in mycursor.fetchall():
	print(x)
#2.2
mycursor.execute("SELECT FirstName,Gender,Salary FROM Employee")
for x in mycursor.fetchall():
	print(x)
#2.3
mycursor.execute("SELECT * FROM Employee ORDER BY FirstName DESC")
for x in mycursor.fetchall():
	print(x)
#2.4
mycursor.execute("DELETE FROM Employee WHERE Age = 34")
mydb.commit()
mycursor.execute("SELECT * FROM Employee")
for x in mycursor.fetchall():
	print(x)
# 3
f = open("python.txt", "r")
print(f.readlines())