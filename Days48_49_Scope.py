year = 2019
def years():
	year = 2020
	print(year)
	def newYear():
		print(year)
	newYear()

years()
print(year)

#---------------------
number = 20
def numbers():
	global number
	number = 10
	print(number)

numbers()
print(number)