print("\t\t\t TO-DO LIST")
tasks=[]
def add_Task():
    task=input("\nENTER THE TASK TO BE ADDED")
    tasks.append(task)
    print("\nTASK SUCCESSFULLY ADDED")
def display_Task():
    i=1
    for j in tasks:
        print(i,")",j)
        i+=1
def remove_Task():
    display_Task()
    sub=input("\nDO YOU WANT TO MARK AS COMPLETE ANY TASK")
    if sub in ('YES','yes'):
        index=int(input("\nENTER THE TASK'S NUMBER TO MARK AS COMPLETE"))
        tasks.pop(index)
    else:
        index=int(input("\nENTER THE TASK'S NUMBER TO DELETE"))
        tasks.pop(index)
def update_Task():
    display_Task()
    index=int(input("\nENTER THE TASK'S NUMBER TO UPDATE IT"))
    new_Task=input("\nENTER THE NEW TASK")
    tasks[index-1]=new_Task
loop_Variable=0
while loop_Variable==0:
    print("\t\t\n1.ADD A TASK\n\t\t2.REMOVE TASK\n\t\t3.UPDATE TASK\n\t\t4.DISPLAY A TASK\n\t\t5.EXIT")
    choice=int(input("\nENTER YOUR CHOICE"))
    if choice==1:
        add_Task()
    elif choice==2:
        remove_Task()
    elif choice==3:
        update_Task()
    elif choice==4:
        display_Task()
    else:
        print("THANK YOU")
        loop_Variable=1
