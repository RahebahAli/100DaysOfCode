#Multiplication table from 1 to 10 for any number taken from user
#Use (lambda) inside function 
def mul (number):
	return lambda a : a *number

LOL =  [mul(i) for i in range(1, 11)]
number = int(input("Enter number : "))
for i in LOL:
	print(i(number))