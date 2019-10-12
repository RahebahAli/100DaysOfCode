class numbers:
	def __init__(self, star, end):
		self.s = star
		self.e = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.s <= self.e:
			x = self.s
			self.s += 1
			return x
		else :
			raise StopIteration


num1 = int(input("Enter the start number: "))
num2 = int(input("Enter the end number: "))
n = numbers(num1,num2)
myiter = iter(n)

for x in myiter:
	print(x)