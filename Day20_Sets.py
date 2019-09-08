# Create a set
languagesSet = {"Java", "Python", "Swift", "C", "C++"}
print(languagesSet)
# display the items
for x in languagesSet:
	print(x)
# Check if "Python" is present in the set
for x in languagesSet:
	if "Python" in languagesSet:
		print("Yes")
		break
# OR
print("Python" in languagesSet)
# To add one item
languagesSet.add("HTML")
print(languagesSet)
# To add more than one item, but it must be inside []
languagesSet.update(["CSS", "JS", "SQL", "Java"])
print(languagesSet)