text = " Please, I want {} sandwishes and {} donutes "
print (text) # Please, I want {} sandwishes and {} donutes

# 1 : After replacing "I" with "We
text2 = text.replace("I", "We")
print (text2) # Please, We want {} sandwishes and {} donutes

# 2 : After the first space is filled with number 5 and the second space by number.7
text3 = text2.format(5, 7)
print (text3) # Please, We want 5 sandwishes and 7 donutes

# 3 : After converting each letter “a” to capital
text4 = text3.replace("a", "A")
print(text4) # PleAse, We wAnt 5 sAndwishes And 7 donutes