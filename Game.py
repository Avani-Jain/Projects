import random

#function for the game 
def Game(you, co):
    if co == you:
        print("Tie")
    elif you == "stone":
        if co == "paper":
            print("You lose")
        if co == "scissor":
            print("You win")
    elif you == "paper":
        if co == "scissor":
            print("You lose")
        if co == "stone":
            print("You win")
    elif you == "scissor":
        if co == "stone":
            print("You lose")
        if co == "paper":
            print("You win")
    
    
play = True
count = 0
while play == True:
    count += 1
    li = ["Stone", "Paper", "Scissor"]
    print(li)
    p1 = input("Enter your choice : ")
    comp = random.choice(li)
    p1_main =p1.lower()
    comp_main = comp.lower()
    if count >= 3:
        e = input("do you want to exit (y/n): ")
        if e=="y":
            break
        elif e != "n" and e!="y":
            break
        else:
            continue

    if p1_main != "stone" and p1_main !="scissor" and p1_main !="paper":
        print("Enter valid value!!")
        continue
    
    print("Computer choice is : ", comp_main) 
    print("\nGame results:")
    Game(p1_main, comp_main)

    #provides a loop if the player wants to play the game again.
    y_or_n = input("Want to play again (y/n): ")
    if y_or_n == "n" or y_or_n != "y":
        play= False
        print("See you again!")
        break
    
