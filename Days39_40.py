#1
def cubic(x, a):
	if (a > 0):sum = x * cubic(x, a-1)
	else:sum = 1 
	return sum

print(cubic(5, 3))

#-----------------------------------
#2
ThisList = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
n = lambda x : x>=0
for x in ThisList :
	if n(x):
		print(x)