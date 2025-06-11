# LIBRARY MANAGEMENT SYSTEM
import sqlite3
connection=sqlite3.connect("LIBRARY.db")
c=connection.cursor()

def creating_table():
    sql_command="""CREATE TABLE user_details(user_name VARCHAR,user_id VARCHAR(10) PRIMARY KEY,password VARCHAR(6),email_id VARCHAR(20),birth_date DATE);"""
    c.execute(sql_command)

user_details={'ABIJITH':[12,1234,[0]]}
book_details={"WINGS OF FIRE:":['ABDUL KALAM',23]}
def getting_user_details():
    user_id=input("ENTER YOUR ID:")
    user_password=input("ENTER THE PASSWORD:")
    email_id=input("ENTER YOUR MAIL-ID")
    current_borrow=[0]
    def inserting_user_details():
        command="""INSERT INTO user_details(user_name,user_id,password,email_id)VALUES("{n}","{id}","{p}","{em}")"""
        sql_command=command.format(n=user_name,id=user_id,p=user_password,em=email_id)
        c.execute(sql_command)
    inserting_user_details()
    return [user_id,user_password,email_id,current_borrow]

def add_books():
    book_name=input("ENTER BOOK NAME:")
    if book_name in book_details:
        print("BOOK ALREADY EXISTS")
        count=int(input("enter the count to be added"))
        book_details[book_name][1]+=count
        print("BOOK COUNT ADDED SUCCESSFULLY")
        print(f"{book_name} was increased to {book_details[book_name][1]}")
    else:
        author_name=input("ENTER THE AUTHOR NAME:")
        book_count=int(input("enter the count of books to be added:"))
        book_details[book_name]=[author_name,book_count]
        print("BOOK ADDED SUCCESSFULLY")
        print(f"{book_name} was added successfully with count {book_details[book_name]}")

def current_borrow():
    user_id=input("ENTER YOUR USER ID")
    book_name=[map(str,input("ENTER THE NAME OF THE BOOKS TO BE BORROWED(SEPERATED BY ,)").split(","))]
    for i in book_name:
        if book_name not in list(book_details.keys()):
            print(f"BOOK {i} IS  NOT AVAILABLE")
    for i in user_details:
        if user_id == user_details[i][0]:
            user_details[i][2]=book_name
    print("BOOK BORROWED WAS NOTED SUCCESSFULLY")
    print(user_details)
def authentication(user_name):
    sql_command="""SELECT user_name,user_id,password from user_details"""
    c.execute(sql_command)
    details=c.fetchall()
    for d in details:
        if d[0] == user_name:
            u_id=input("ENTER YOUR USER_ID:")
            p=input("ENTER YOUR PASSWORD:")
            if d[1]==u_id and d[2]==p:
                print("USER VERIFIED SUCCESSFULLY")
        
while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1.add user")
    print("2.add books")
    print("3.list user")
    print("4.list books with availability status")
    print("5.borrowing of books")
    print("6.EXIT")
    try:
        choice=int(input("ENTER YOUR CHOICE(1-4):"))
        if choice==1:
            user_name=input("ENTER YOUR NAME:")
            user_details[user_name]=getting_user_details()
            print("USER ADDED SUCCESSFULLY")


        elif choice==2:
            add_books()
    
        elif choice==3:
            for i in user_details:
                print(i)
        elif choice==4:
            for i in book_details:
                print(f"BOOK NAME: {i} with availabiltiy of {book_details[i][1]}")
        elif choice==5:
            current_borrow()
        elif choice==6:
            break
    except ValueError:
        print("PLEASE ENTER A VALUE FROM 1-6")