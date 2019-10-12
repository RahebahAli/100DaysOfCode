class Parent:
	def __init__(self, fname, lname ):
		self.fname = fname
		self.lname = lname

	def display(self):
		print(self.fname + " " + self.lname)


class Child(Parent):
	def __init__(self, fname, lname, age):
		Parent.__init__(self, fname, lname )
		self.age = age


	def show(self):
		print(self.fname + " " + self.lname)
		print(self.age)


class AA(Child):
	def __init__(self, fname, lname, age):
		super().__init__( fname, lname, age )


p = Parent('Ali', 'Ahmad')
p.display()

c = Child('Amal', 'Saad', 23)
c.show()

a = AA("Lena", "Khaled", 20)
a.display()

