def binary_Sort_Algorithm(loop):
    if loop==0:
        initial_Value=int(input("ENTER THE INITIAL VALUE"))
        final_Value=int(input("ENTER THE FINAL VALUE"))
    else:
        pass
    l1=[]
    for i in range(initial_Value,final_Value+1):
        l1.append(i)
    print(l1)
    length=len(l1)
    mid_Value=l1[length//2]
    print("THE MIDVALUE IN THIS RANGE IS ",mid_Value)
    initial_Value=mid_Value
    print(initial_Value)
loop_Variable=0
while True:
    choice=int(input("DO YOU WANT TO CALL THE FUNCTION THEN PRESS 1"))
    if choice==1:
        binary_Sort_Algorithm(loop_Variable)
        loop_Variable+=1
    else:
        break
