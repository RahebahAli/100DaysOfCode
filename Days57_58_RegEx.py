import re
text = "Always remember that sunset does not prevent sunrise at all"
#Check if the string starts with "Always" and ends with "all":
x = re.search("^Always.*all$", text)
if(x):
	print("YES")
else:
	print("NO")
#Check if  the string DOES NOT contain digits:
d = re.findall("\D", text)
if(d):
	print("YES")
else:
	print("NO")

#heck if the string contains a white space character:
s = re.findall("\s", text)
if(s):
	print("YES")
else:
	print("NO")

#Check if "ber" is present at the end of a WORD

y = re.findall(r"t\b", text)

print(y)

if (y):
  print("YES")
else:
  print("NO")

#Check if the string has any A, s, or o characters:

z = re.findall("[Aso]", text)

print(z)

if (z):
  print("Yes")
else:
  print("NO")

sp = re.split("e",text)
print(sp)

sp = re.split("\s",text)
print(sp)