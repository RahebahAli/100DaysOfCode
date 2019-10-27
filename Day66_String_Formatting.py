level = input("Enter your level : ")
name = str(input("Enter your name : "))
age = int(input("Enter your age : "))

text = "hello, {1} \nName : {1}, Age : {2}, Level : {0} "
print(text.format(level, name, age))

text1 = "Hello, {name}"
print(text1.format(name="Ali"))