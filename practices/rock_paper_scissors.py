#ER 2nd Rock paper scissors
import random

player_wins = 0
computer_wins = 0
while player_wins <=6 or computer_wins <=6:
    comp = random.randint(1,4)
    player = int(input("Do you choose rock (1), paper (2), or scissors(3)? (Type 4 to exit)"))
    if player == 1 and comp != 2:
        print("You Win!")
        player_wins +=1
        continue
    else:
        print("Computer Wins!")
    if player == 2 and comp != 3:
        print("You Win!")
        player_wins +=1
        continue
    else:
        print("Computer Wins!")
        computer_wins +=1
    if player == 3 and comp != 1:
        print("You Win!")
        player_wins +=1
        continue
    else:
        print("Computer Wins!")
        computer_wins +=1
    if player == 4:
        break
else:

