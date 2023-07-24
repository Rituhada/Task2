import random
print("-------welcome-------")
user_score=0
comp_score=0
ties=0
name=input("Enter your name = ")
print("")

print("Hi " + name + " these are the Rules of game : ")
print("""
1. Paper vs Rock     -> Paper
2. Rock  vs scissors -> Rock
3. Scissors vs Paper -> Scisors""")
while True:
    print(""" Choices are:
    1. Rock
    2.Paper
    3.Scissors""")

    choice=int(input("enter your choice : "))
    while choice >3 or choice <1 :
        choice = int(input("enter the valid input : "))
    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_choice="Scissors"
    print("the user's choice is",user_choice)
    print("now it's computer turn")

    computer= random.randint(1,3)

    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissors"
    print("the computer's choice is", comp_choice)

    if ((user_choice=="Paper" and comp_choice=="Rock")or (user_choice=="Rock" and comp_choice=="Paper")):
       print("Paper wins")
       result="Paper"
    elif ((user_choice=="Scissors" and comp_choice=="Rock")or (user_choice=="Rock" and comp_choice=="Scissors")):
        print("Rock wins")
        result="Rock"
    elif(user_choice==comp_choice):
        print("it's tie")
        result="Tie"
    else:
        print("scissors wins")
        result="scessiors"
    if result=="Tie":
        ties+=1
    elif result==user_choice:
        print("user wins")
        user_score+=1
    else:
        print("computer wins")
        comp_score+=1

    print("scores are")
    print(name," score is" ,user_score)
    print("computer's score is",comp_score)
    print("tie's are",ties)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
print("Game over")
print("Thanks for playing",name)






