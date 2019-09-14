# 1
ThisSet = {1, 3, 5, 7, 8 }
print(ThisSet)

ThisSet.add(4)
ThisSet.update([8, 12])
print(ThisSet)


if 8 in ThisSet:
	print("YES")
	ThisSet.remove(8)
	print(ThisSet)

ThisSet.clear()
print(ThisSet)

# 2
ThisDictionary = dict(Name="pigeon", Type="bird")
ThisDictionary["SkinCover"] = "feathers"

'''
OR
ThisDictionary["Name"] = "pigeon"
ThisDictionary["Type"] = "bird"
'''

print(ThisDictionary["Type"])

ThisDictionary["SkinCover"] = "quilt"
print(ThisDictionary)