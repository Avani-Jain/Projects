import random

li = []
i= 1
while i in range(1, 7):
    li.append(i)
    i+=1

class dice:
    def random_option(self):
        option = random.choice(li)
        print("And the number is : ", option)
        self.option = option

yes_or_no = True

while yes_or_no == True:
    choice = int(input("Enter your guess from 1 to 6: "))
    start = dice()
    start.random_option()
    if choice == start.option:
        print("Great Guess!!! Nailed it!")
    elif choice<=6 and choice>=1 and choice!=start.option:
        print("Wrong guess! Better luck next time")
    else:
        print("Enter a valid value")
    play = input("Do you want to play again? (yes/no)").lower()
    if play == "yes" or play =="y":
        continue
    elif play == "no" or play == "n":
        break
    else:
        print("Enter valid input.")
        break 
