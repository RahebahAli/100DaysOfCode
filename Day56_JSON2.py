import json

Student = {'ID': 1102, 'Name': 'Ali', 'Level': 'Six', 'Age': 20}
sjson = json.dumps(Student)
print (sjson)

sjsonI = json.dumps(Student, indent=4)
print(sjsonI)

sjsonIS = json.dumps(Student, indent=4, separators=(".", "="))
print(sjsonIS)

sjsonISK = json.dumps(Student, indent=4, separators=(".", "="), sort_keys=True)
print(sjsonISK)