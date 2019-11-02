import os
file = open("test.txt", "x")

file = open("test.txt", "w")
file.write("Your life always be full of challenges, so it's best to decide living happy in spite of all the challenges")
file.close()

file = open("test.txt", "r")
print(file.read(39))

file = open("test.txt", "a")
file.write("\nIs impossible to please people in all things ... and therefore our only concern should be limited to satisfy our consciences")
file.close()

file = open("test.txt", "r")
print(file.readline())
print(file.read())

#os.remove("test.txt")