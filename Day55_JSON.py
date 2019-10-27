import json 
# Convert from Python to JSON : ( json.dumps() )
Fruits = ["apple", "banana", "orange"] #List
Fjson =  json.dumps(Fruits) 
print(Fjson)
Student = {"ID":1102, "Name":"Ali"} # Dictionary
Sjson = json.dumps(Student)
print(Sjson)

# Convert from JSON to Python: ( json.loads() )
Fpython = json.loads(Fjson)
print(Fpython)
Spython = json.loads(Sjson)
print(Spython)