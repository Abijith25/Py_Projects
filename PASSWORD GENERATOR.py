import random
import string
print("\t\t\t\t PASSWORD GENERATOR")
def password_Only_Numbers():
    length=int(input("ENTER THE LENGTH OF THE PASSWORD"))
    password=[]
    for i in range(1,length+1):
        random_int=random.randint(0, 9)
        password.append(random_int)
    print("THE PASSWORD IS ,",)
    for number in password:
        print(number, end=' ')
def password_Only_Letters():
    length=int(input("ENTER THE LENGTH OF THE PASSWORD"))
    password_1= [random.choice(string.ascii_letters) for _ in range(length+1)]
    print("THE PASSWORD IS ")
    for number in password_1:
        print(number, end=' ')
def password_With_Special_Characters():
    length=int(input("ENTER THE LENGTH OF THE PASSWORD"))
    password_Characters=string.ascii_letters + string.digits + string.punctuation
    password_2=[random.choice(string.printable)for _ in range(length+1)]
    for number in password_2:
        print(number, end=' ')
while True:
    print("\t\t 1.PASSWORD ONLY WITH NUMBERS")
    print("\t\t 2.PASSWORD ONLY WITH ALPHABETS")
    print("\t\t 3.PASSWORD WITH SPECIAL CHARACTERS")
    choice=int(input("ENTER THE CHOICE"))
    if choice==1:
        password_Only_Numbers()
    elif choice==2:
        password_Only_Letters()
    elif choice==3:
        password_With_Special_Characters()
    option=input("\n DO YOU WANT TO CONTINUE")
    if option in ('NO','no'):
        print("\t\t\t\tTHANK YOU")
        break
