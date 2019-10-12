class library:
	def __init__(self):
		self.book = 300
		self.shelf = 45

class science_section(library):
	def __init__(self):
		super().__init__()
		self.name = "Physics books"

	def display(self):
		print("book : "+str(self.book)+"\nshelf : "+str(self.shelf)+"\nname : "+str(self.name)+"\n")


x = science_section()
x.display()

x.book = 20
x.shelf = 4
x.display()