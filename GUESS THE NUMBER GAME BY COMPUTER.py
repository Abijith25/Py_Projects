import tkinter
from tkinter.font import Font

root = tkinter.Tk()
root.title("GUESSING GAME")
root.geometry('500x500')
root.resizable(height=False, width=False)  # Use 'False' instead of "false"
myfont = Font(family="times", size=25, weight="bold", slant="italic")
upper_Limit=1
lower_Limit=100
def new_Window():
    global second
    global upper_Limit
    global lower_Limit
    global mid_Value
    att = 1
    ans=0
    def higher():
        nonlocal ans
        nonlocal att # Use 'nonlocal' to modify the outer 'att'
        if att==1:
            upper_Limit=50
            lower_Limit=101
        else:
             
        l2=[]
        for i in range(upper_Limit,lower_Limit):
            l2.append(i)
        length=len(l2)
        ans=l2[length//2]
        lab2.configure(text="is it %s" % ans)
        att += 1
        upper_Limit=101
        lower_Limit=length
        mid_Value=ans
        print(upper_Limit,lower_Limit,mid_Value)
    def lower():
        nonlocal ans
        nonlocal att 
        limit=0
        l3=[]
        for i in range(1,limit):
            l3.append(i)
        length_1=len(l3)
        ans_1 = round(length_1/2)
        lab2.configure(text="is it %s" % ans_1)
        limit= ans_1
        print(limit)
        nonlocal att  
        att += 1
    def found():
        lab2.configure(text="YOUR NUMBER IS GUESSED IN %d ATTEMPT" % att)# Use '%d' for integers        
    second = tkinter.Toplevel()
    second.title("GUESSING YOUR NUMBER")
    second.geometry("750x750")
    lab1 = tkinter.Label(second,
                         text="GUESS A NUMBER WITHIN HUNDRED",
                         font=myfont)  # Remove the quotes around 'myfont'
    lab1.pack()
    lab2 = tkinter.Label(second, text="is it 50?", font=myfont)  # Remove the quotes around 'myfont'
    lab2.pack()
    my_Button_1 = tkinter.Button(second,
                                 text="HIGHER",
                                 font=myfont,  # Remove the quotes around 'myfont'
                                 command=higher,
                                 bg="red",
                                 fg="yellow")
    my_Button_1.place(x=75, y=20)
    my_Button_1.pack()
    my_Button_2 = tkinter.Button(second,
                                 text="LOWER",
                                 font=myfont,  # Remove the quotes around 'myfont'
                                 command=lower,
                                 bg="red",
                                 fg="yellow")
    my_Button_2.place(x=100, y=19)
    my_Button_2.pack()
    my_Button_3 = tkinter.Button(second,
                                 text="YES",
                                 font=myfont,  # Remove the quotes around 'myfont'
                                 command=found,
                                 bg="red",
                                 fg="yellow")
    my_Button_3.place(x=80, y=21)
    my_Button_3.pack()
    second.deiconify()

my_Button = tkinter.Button(root,
                           text="PLAY GAME",
                           command=new_Window,
                           bg="green",
                           fg="black")
my_Button.place(x=80, y=30)
my_Button.pack()
root.mainloop()

    
    
    
