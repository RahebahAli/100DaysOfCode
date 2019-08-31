# Python Logical Operators
# I want to make sure the age is between 20 and 40
age = int(input("Enter your age : "))
if age >= 20 and age <= 40 :
    print("Accepts")
else :
    print ("Does not accept")

x = 6
print(not(x<0 or x>10))

########################
Fruits = ["apple", "banana", "orange"]
Fruits2 = ["apple", "banana", "orange"]
Fruits3 = Fruits

#Python Identity Operators
print(Fruits is Fruits2)
print(Fruits is not Fruits2)
print(Fruits is Fruits3)
print(Fruits is not Fruits3)

#Python Membership Operators
print("apple" in Fruits)
print("banana" not in Fruits)
