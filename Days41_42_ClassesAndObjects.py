#Create class by using class Keyword
class student:
	def __init__(self, name, age, level):
		self.name = name
		self.age = age
		self.level = level

	def hi(a):
		print("Hello, " + a.name )

#Crreate object
s1 = student("Ali", 20, 6)
s1.hi()
print (s1.age )
#Change the age in the object s1
s1.age = 21
print(s1.age)
#Delete
del s1.name
del s1