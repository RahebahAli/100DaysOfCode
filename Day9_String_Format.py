from string import Template

text = "The value of {} KD is {} SR"
KD = float(input("Please enter any number to convert it from KD to SR :"))
SR = KD * 12.34

#The first way
print(text.format(KD,SR))

#The second way
print(f"The value of {KD} KD is {SR} SR")

#The third way
t = Template("The value of $KD KD is $SR SR")
print(t.substitute(KD=KD, SR=SR))