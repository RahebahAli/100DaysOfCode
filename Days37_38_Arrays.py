#Arrays are used to store multiple values in one single variable.
number = []
number = [x for x in range(1,11)]
print(len(number))
number.append(11)
print(number)
number[5] = 12
number.pop(1)
number.pop()
number.remove(5)
print(number)