import mysql.connector

mydata = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
print(mydata)

mycursor = mydata.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)