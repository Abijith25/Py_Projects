print("\t\t FIND THE LARGEST NUMBER")
terms=int(input("ENTER THE NO.OF.TERMS "))
value_List=[]
for i in range(1,terms+1):
    value=int(input("ENTER THE VALUE :"))
    value_List.append(value)
print("THE VALUES YOU HAVE ENTERED IS \n",value_List)
print("LARGEST VALUE IN THE LIST IS ",max(value_List))
