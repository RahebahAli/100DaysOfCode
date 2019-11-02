import mysql.connector

mydata = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="mydatabase")


mycursor = mydata.cursor()
#Insert singl row.
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Ali", "Buraydah")
mycursor.execute(sql, val) 
mydata.commit()
print(mycursor.rowcount, "record inserted.")
#Insert multiple rows.
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
("Ahmad", "Buraydah"),
("Saad", "Buraydah"),
("Fahad", "Buraydah"),
("tala", "Buraydah")]
mycursor.executemany(sql, val)
mydata.commit()
print(mycursor.rowcount, "record inserted.")
#Insert singl row and display id for it.
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Bana", "Buraydah")
mycursor.execute(sql, val) 
mydata.commit()
print("1 record inserted, ID :", mycursor.lastrowid)
# Select
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)

mycursor.execute("SELECT * FROM customers WHERE id = 5")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)

mycursor.execute("SELECT * FROM customers WHERE name like '%ad%'")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)