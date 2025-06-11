print("LISTING OUT THE NO.OF.CHARACTER TYPES IN A STRING")
space=upper_Case=lower_Case=other_Character=0
string=input("\n \n \t\t ENTER A STRING TO COUNT IT'S NO.OF.CHARACTERS :")
for i in string:
    if i==" ":
        space+=1
    elif i.isupper():
        upper_Case+=1
    elif i.islower():
        lower_Case+=1
    else:
        other_Character+=1
print("\n THE NO.OF.UPPERCASE CHARACTERS ARE : ",upper_Case)
print("\n THE NO.OF.LOWERCASE CHARACTERS ARE : ",lower_Case)
print("\n THE NO.OF.SPACE ARE : ",space)
print("\n THE NO.OF.OTHER CHARACTERS ARE : ",other_Character)
