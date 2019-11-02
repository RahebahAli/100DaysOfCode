import mysql.connector

mydata = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="mydatabase")

mycursor = mydata.cursor()
mycursor.execute("SELECT * FROM customers ORDER BY name ")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

mycursor.execute("SELECT * FROM customers ORDER BY name DESC")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

mycursor.execute("DELETE FROM customers WHERE name = 'tala'")
mydata.commit()
print(mycursor.rowcount, "record(s) deleted")

# mycursor.execute("DROP TABLE customers")
# OR
# mycursor.execute("DROP TABLE IF EXISTS customers")