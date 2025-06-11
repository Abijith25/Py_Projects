print("\n \n \n\n CREATING A PYTHON PROGRAM FOR FACTORIAL")
def factorial():
    try:
        value=int(input("ENTER THE NUMBER : "))
        def fact():
            ans=1
            for i in range(1,value+1):
                ans*=i
            return ans
        answer=print("\n WRONG INPUT") if value<0  else fact()
        print("\n THE ANSWER IS ,",answer)
    except ValueError:
        print("\n \n PLEASE ENTER THE VALID INPUT")
factorial()
