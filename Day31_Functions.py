def sum(x=0, y=0):
	print (x+y)


sum(4, 8) # 12
sum(-4, 5) # 1
sum(6) # 6
sum() # 0

#-------------------
def square(x):
	print(x*x)


square(8) # 64
square(3) # 9

#-------------------
def tri_recursion(k):
  if(k>0):
    result = k*tri_recursion(k-1)
  else:
    result = 1
  return result


p = int(input("Enter number : "))
print(tri_recursion(p))