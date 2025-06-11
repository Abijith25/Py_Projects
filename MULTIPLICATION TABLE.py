print("PRINT THE MULTIPLICATION TABLE")
table=int(input("ENTER THE NUMBER TO PRODUCE IT'S TABLES"))
end_Value=int(input("ENTER THE LAST RANGE OF THE TABLE"))
for i in range(1,end_Value+1):
    print(i,"*",table,"=",i*table)
