# 1
first = str(input("Enret the first letter of your name : "))
last = str(input("Enret the last letter of your name : "))
print ("The first letter from your name ", first, "\nThe last letter from your name ",last)

# 2
name = "Ahmad Ali"
balance = 53.44 
text = "Dear {}, Your current balance is {} $"
print(text.format(name, balance))

# 3
number =int(input("Entre number of items : "))
num = []
for x in range(number):
	num.append(int(input("Entre number : ")))
print(num)