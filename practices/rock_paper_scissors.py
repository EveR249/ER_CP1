#ER 2nd Rock paper scissors
import random

player_wins = 0
computer_wins = 0

#rock = """  ____
# /    \ 
#|      |
# \____/ """


#paper = """_____
#|----|
#|----|
#|____|"""

#scissors = """/|  |\ 
# \|  |/
#   \/
#  //\\\ 
# ()  ()"""

print("Welcome to Rock, Paper, Scissors.")
#print(f"{rock} \n {paper} \n\n {scissors}")

while player_wins >= 0:
    comp = random.randint(1,4)
    player = int(input("Do you choose rock (1), paper (2), or scissors(3)? (Type 4 to exit)"))
    if player == 1 and comp != 2:
        print("You won!")
        player_wins +=1
        print(f"You have {player_wins} wins! The computer has {computer_wins} wins!")
    if player == 1 and comp == 2:
        print("Computer won!")
        computer_wins +=1
        print(f"You have {player_wins} wins! The computer has {computer_wins} wins!")
    if player == 2 and comp != 3:
        print("You won!")
        player_wins +=1
        print(f"You have {player_wins} wins! The computer has {computer_wins} wins!")
    if player == 2 and comp == 3:
        print("Computer won!")
        computer_wins +=1
        print(f"You have {player_wins} wins! The computer has {computer_wins} wins!")
    if player == 3 and comp != 1:
        print("You won!")
        player_wins +=1
        print(f"You have {player_wins} wins! The computer has {computer_wins} wins!")
    if player == 3 and comp == 1:
        print("Computer won!")
        computer_wins +=1
        print(f"You have {player_wins} wins! The computer has {computer_wins} wins!")
    if player == 4:
        print(f"Your total is {player_wins} wins! The computers total is {computer_wins} wins!")
        break

print("Thank you for playing!")