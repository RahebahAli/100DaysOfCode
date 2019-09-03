Fruits = ["Apple", "banana", "orange", "Strawberries"]

print(Fruits) 
# To calculates the number of items a list
print(len(Fruits))
# To add an item in last the list
Fruits.append("Grape")
print(Fruits)
# To add an item at the specified index
Fruits.insert(4, "apple")
print(Fruits)
# orts thre list
Fruits.sort()
print(Fruits)
# To removes the specified item
Fruits.remove("apple")
print(Fruits)
# To removes the specified item or last item
Fruits.pop()
print(Fruits)
Fruits.pop(2)
print(Fruits)
# copy a list
Fruits2 = Fruits.copy() # Same as : Fruits2 = list(Fruits)
print(Fruits2)
# To empties the list
Fruits.clear()
print(Fruits)
# To create a new list.
Fruits3 = list(("Apple", "Banana", "Orange", "Strawberries", "Grape"))
print(Fruits3)