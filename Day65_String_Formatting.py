name = str(input("Enter your name : "))
age = int(input("Enter your age : "))
level = input("Enter your level : ")

text = "Name : {}, Age : {}, Level : {} "
print(text.format(name, age, level))