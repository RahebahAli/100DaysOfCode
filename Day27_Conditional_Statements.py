# Specifies odd and even numbers
Number = int(input("Enter number : "))
print("Even") if Number%2 == 0 else print("odd")

# A calculator 
Number1 = int(input("Enter number : "))
Number2 = int(input("Enter number : "))
operation = str(input("Enter operation : "))
if operation == "+":
	print(Number1 + Number2)
elif operation == "-":
	print(Number1 - Number2)
elif operation == "*":
 	print(Number1 * Number2)
elif operation == "/":
 	print(Number1 / Number2)

# Ages are approved from 1 year to 20 years
age = int ( input ("Enter your age :")) 
if age > 0 and age <= 20:
	print("OK")
else :
	print("NO")