languagesList = ["java", "Python", "Swift"]
print(languagesList)

print(len(languagesList))

languagesList.append("c")
print(languagesList)

languagesList.insert(2, "C++")
print(languagesList)

languagesList.sort()
print(languagesList)

print(languagesList.count("c"))

languagesList.reverse()
print(languagesList)

languagesList.extend("sql")
print(languagesList)

languagesList.pop(1)
print(languagesList)

ThisList = languagesList.copy()
languagesList.remove("Swift")
print("ThisList : ", ThisList)
print("languagesList : ", languagesList)

ThisList.cleare()
print(ThisList)

languagesTuple = tuple(languagesList)
print(languagesTuple)

if 'Python' in languagesTuple:
	print("Yes, 'Python' is in the languagesTuple Tuple")