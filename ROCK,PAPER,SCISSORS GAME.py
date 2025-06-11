import random
print("\t\t\t\tROCK PAPER SCISSORS GAME")
def game():
    options = ['Rock', 'Paper', 'Scissors']
    random_choice = random.choice(options)
    print("\n1.ROCK\n2.PAPER\n3.SCISSORS")
    choice=input("\n\tENTER THE CHOICE")
    print("\nTHE COMPUTER'S CHOICE IS ",random_choice)
    if choice in ('rock','ROCK','Rock') and random_choice in ('Paper','Scissors'):
        if random_choice=="Paper":
            print("COMPUTER WINS")
        else:
            print("YOU WON")
    elif choice in ('PAPER','Paper','paper') and random_choice in ('Rock','Scissors'):
        if random_choice=="Rock":
            print("YOU WON")
        else:
            print("COMPUTER WINS")
    elif choice in ('SCISSORS','Scissors','scissors') and random_choice in ('Rock','Paper'):
        if random_choice=="Paper":
            print("YOU WON")
        else:
            print("COMPUTER WINS")
    else:
        print("THE MATCH ENDS IN DRAW")
game()
loop_Variable=0
while loop_Variable==0:
    regame=input("DO YOU WANT TO PLAY AGAIN")
    if regame in ('YES','Yes','yes'):
        game()
    else:
        print("\t\t\t\tTHANK YOU")
        loop_Variable=1
