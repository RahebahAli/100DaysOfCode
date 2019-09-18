from random import randint

x = int(randint(0, 100))
y = r = 0
''' The program informs the random number and asks the user to enter 
a number or a group of numbers (more attempts are 10) their total
is the random number and if the sum of the entered numbers is larger
immediately stop the program and print an error'''
while y < 10:
	s = int(input(f"Enter any numbers,but the sum equle {x} (In ten attempts) : "))
	r = r + s
	if r == x:
		print("Goooood")
		break
	elif r > x:
		print("Noooooo")
		break
	y += 1

else :
	print("Wrong, try again")
