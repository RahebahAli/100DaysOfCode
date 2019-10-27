try:
	age = int(input("Enter your age : "))
except ValueError:
	print("must enter integer ")
except:
	print("Something else went wrong")