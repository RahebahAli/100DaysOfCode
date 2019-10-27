# 1
import json
Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
Days_JSON = json.dumps(Days)
print(Days_JSON) 

#2
import re 
text = "data is the new oil "
t = re.search("data", text)
# print YES if the word is exist, and print NO if the word is not exist
if(t):
	print("YES")
else:
	print("NO")
# print the word
print(t.group())