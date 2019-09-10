LanguagesSet = {'HTML', 'Java', 'C++', 'CSS', 'SQL', 'Swift', 'Python', 'C', 'JS'}
# To take copy from a set LanguagesSet
Languages = LanguagesSet.copy()
print(Languages)
# To calculetor an items in the set
print(len(LanguagesSet))
# to delete an item
LanguagesSet.discard("C")# If the item does not exist, it will not display the error message
print(LanguagesSet)
# OR 
LanguagesSet.remove("CSS")#If the item does not exist, it displays the error message
print(LanguagesSet)
# To displays the differences between the sets
print(Languages.difference(LanguagesSet))
print(Languages)
# To displays the differences between the sets, and stores it
Languages.difference_update(LanguagesSet)
print(Languages)
#To returns repeating items in both sets
Languages.intersection(LanguagesSet)
print(Languages)
# To delete the last item
x = Languages.pop()
print(x)
# To delete all the items in the set
Languages.clear()
print(Languages)
# To delete the set
del Languages
print(Languages)