import re

text = "Be the person who inspires positive energy everywhere."

e = re.sub("e", "E",text)
print(e)

ee = re.sub("\s" ,"," ,e ,4)
print(ee)


x = re.search(r"\bE\w+", e)
x1 = re.search("E", e)
print(x.group())
print(x.string)
print(x1.span())