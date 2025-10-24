#ER 2nd COMBAT PROGRAM
import random

health = 0
defense = 0

def user_turn():
    print("What would you like to do?")
    if fight_class == 1:
        move = int(input("1. Normal Attack \n 2. Drink healing potion (regain 9 health) \n 3. Flee (may or may not get away)"))
        if move == 1:
            attack = random.randint(1,21) + 3
            dmg = random.randint(1,9) + 4
            if attack > defense:


print("Welcome to training! First I need to know some things about you!")
name = input("What is your name? ")

while True:
    fight_class = int(input("What class of fighter are you? \n 1. Fighter \n 2. Mage \n 3. Rogue \n"))
    if fight_class == 1:
        print("Great, here are your stats!")
        health = 30
        defense = 14
        print(f"Health:{health}")
        print(f"Defense:{defense}")
        print(f"Attack: D20 + 3")
        print(f"Damage: D8 + 4")
        break
    elif fight_class == 2:
        print("Great, here are your stats!")
        health = 20
        defense = 10
        print(f"Health:{health}")
        print(f"Defense:{defense}")
        print(f"Attack: D20 + 4")
        print(f"Damage: D8 + 5")
        break
    elif fight_class == 3:
        print("Great, here are your stats!")
        health = 25
        defense = 12
        print(f"Health:{health}")
        print(f"Defense:{defense}")
        print(f"Attack: D20 + 5")
        print(f"Damage: D8 + 3")
        break
    else:
        print("Invalid, try again.")
        continue

print("You are being attacked by Goblin!")

turn = random.randint(1,3)

while True:
    if turn == 1:
        print("You go first!")
        user_turn()
        turn +=1
    else:
        print("The Goblin moves first!")
        monster_turn()
        turn -=1