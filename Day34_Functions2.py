'''Can send arguments >> key = value .
This way the order of the arguments does not matter.'''
def people(man, woman):
	print("The man is : " + man + "\n The woman is : " + woman)
	

people(woman="Amal", man="Ali")
#---------------------------------------
#If the number of arguments is unknown, add a * before the parameter name.
#Use return in the function and use print in call the function
def Maximum(*number):
	for x in number:
		y = max(number)
	return y


print(Maximum(2, 4, 5, 8, 1, 10, 9, 3))
#---------------------------------------
'''Python accepts function recursion, 
which means a defined function can call itself'''
def rep(number):
	if(number > 0):
		total = number * rep(number - 1)
	else:
		total = 1
	return total


t = rep(5)
print(t)