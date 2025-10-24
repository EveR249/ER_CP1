#ER 2nd COMBAT PROGRAM
import random

health = 0
defense = 0
monster_hp = 40
monster_defense = 10
run = 0

def user_turn():
    print("What would you like to do?")
    if fight_class == 1:
        move = int(input("1. Normal Attack \n 2. Drink healing potion (regain 9 health) \n 3. Flee (may or may not get away) \n"))
        if move == 1:
            attack = random.randint(1,21) + 3
            dmg = random.randint(1,9) + 4
            if attack > monster_defense:
                goblin_hp -= dmg
                print(f"You hit! The Goblin now has {goblin_hp} health left!")
            else:
                print("You missed!")
        elif move == 2:
            health  = health +9
        elif move == 3:
            run = random.randint(1,21)
            if run >12:
                print("You escaped!")
    elif fight_class == 2:
        move = int(input("1. Normal Attack (must skip a turn to charge) \n 2. Drink healing potion (regain 9 health) \n 3. Flee (may or may not get away)"))
        if move == 1:
            monster_turn()
            attack = random.randint(1,21) + 4
            dmg = random.randint(1,9) + 5
            if attack > monster_defense:
                goblin_hp -= dmg
                print(f"You hit! The Goblin now has {goblin_hp} health left!")
            else:
                print("You missed!")
        elif move == 2:
            health +=9
        elif move == 3:
            run = random.randint(1,21)
            if run >12:
                print("You escaped!")
    else:
        move = int(input("1. Normal Attack \n 2. Drink healing potion (regain 9 health) \n 3. Flee (may or may not get away)"))
        if move == 1:
            attack = random.randint(1,21) + 5
            dmg = random.randint(1,9) + 3
            if attack > monster_defense:
                goblin_hp -= dmg
                print(f"You hit! The Goblin now has {goblin_hp} health left!")
            else:
                print("You missed!")
        elif move == 2:
            health +=9
        elif move == 3:
            run = random.randint(1,21)
            if run >12:
                print("You escaped!")

def monster_turn():
    monster_attack = random.randint(1,21) +2
    if monster_attack > defense:
        health = health - monster_attack
        print(f"The Goblin clobbered you! Your health is now {health}")
    else:
        print(f"The Goblin missed!")

                
        

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

while health >0 and monster_hp >0:
    if run > 16:
        break
    elif turn == 1:  
        print("Your turn!")
        user_turn()
        turn +=1
    else:
        print("The Goblin's turn!")
        monster_turn()
        turn -=1
else:
    if monster_hp == health:
        print("You both died!")
    elif monster_hp > health:
        print("The Goblin defeated you!")
    else:
        print("You defeated the Goblin!")