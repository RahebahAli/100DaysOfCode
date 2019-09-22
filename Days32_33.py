A = []
B = []
O = E = 0

for x in range(20):
	if O in range(2, 18) and O%2 != 0 :
		A.append(O)
	O += 1

for x in range(20):
	if E in range(2, 18 ) and E%2 == 0 :
		B.append(E)
	E += 1

print(A)
print(B)


for x in A:
	for y in B:
		print(x, y)