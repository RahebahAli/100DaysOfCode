import mysql.connector

mydata = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="mydatabase")

mycursor = mydata.cursor()

mycursor.execute("UPDATE customers SET address = 'Unaizah' WHERE name = 'Ahmad'") 
mydata.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor.execute("SELECT * FROM customers LIMIT 2 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute( "SELECT \
  customers.name AS customers, \
  supervisor.name AS supervisor \
  FROM customers \
  JOIN supervisor ON customers.supID = supervisor.id")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)