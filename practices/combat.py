#ER 2nd COMBAT PROGRAM
import random

health = 0
defense = 0
monster_hp = 40
monster_defense = 10
run = 0

def user_turn(health, monster_hp, monster_defense, run, turn):
    print("What would you like to do?")
    if fight_class == 1:
        move = int(input("1. Normal Attack \n 2. Drink healing potion (regain 9 health) \n 3. Flee (may or may not get away) \n 4. Wild attack (More powerful, but damages you) \n"))
        if move == 1:
            attack = random.randint(1,20) + 3
            dmg = random.randint(1,8) + 4
            if attack > monster_defense:
                monster_hp = monster_hp - dmg
                return print(f"You hit! The Goblin now has {monster_hp} health left!")
            else:
                return print("You missed!")
        elif move == 2:
            health +=9
            return print(f"Your health is now {health}")
        elif move == 3:
            run = random.randint(1,20)
            if run >16:
                turn = "over"
                return turn
        elif move == 4:
            attack = random.randint(1,20) + 3
            dmg = random.randint(1,8) + 8
            if attack > monster_defense:
                monster_hp = monster_hp - dmg
                health = health - 4
                return print(f"You hit! The Goblin now has {monster_hp} health left! \n You have {health} health left!")
                
            else:
                return print("You missed!")
    elif fight_class == 2:
        move = int(input("1. Normal Attack (must skip a turn to charge) \n 2. Drink healing potion (regain 9 health) \n 3. Flee (may or may not get away) \n 4. Wild attack (More powerful, but damages you \n"))
        if move == 1:
            monster_turn(health, defense)
            attack = random.randint(1,20) + 4
            dmg = random.randint(1,8) + 5
            if attack > monster_defense:
                monster_hp = monster_hp - dmg
                print(f"You hit! The Goblin now has {monster_hp} health left!")
            else:
                print("You missed!")
        elif move == 2:
            health +=9
            return print(f"Your health is now {health}")
        elif move == 3:
            run = random.randint(1,20)
            if run >16:
                turn = "over"
                return turn
        elif move == 4:
            attack = random.randint(1,20) + 5
            dmg = random.randint(1,8) + 9
            if attack > monster_defense:
                monster_hp = monster_hp - dmg
                health = health - 5
                return print(f"You hit! The Goblin now has {monster_hp} health left! \n You have {health} health left!")
    else:
        move = int(input("1. Normal Attack \n 2. Drink healing potion (regain 9 health) \n 3. Flee (may or may not get away) \n 4. Wild attack (More powerful, but damages you \n"))
        if move == 1:
            attack = random.randint(1,20) + 5
            dmg = random.randint(1,8) + 3
            if attack > monster_defense:
                monster_hp = monster_hp - dmg
                print(f"You hit! The Goblin now has {monster_hp} health left!")
            else:
                print("You missed!")
        elif move == 2:
            health +=9
            return print(f"Your health is now {health}")
        elif move == 3:
            run = random.randint(1,20)
            if run >16:
                turn = "over"
                return turn
        elif move == 4:
            attack = random.randint(1,20) + 5
            dmg = random.randint(1,8) + 7
            if attack > monster_defense:
                monster_hp = monster_hp - dmg
                health = health - 3
                return print(f"You hit! The Goblin now has {monster_hp} health left! \n You have {health} health left!")

def monster_turn(health, defense):
    monster_attack = random.randint(1,20) +2
    if monster_attack > defense:
        health = health - monster_attack
        print(f"The Goblin clobbered you! Your health is now {health}")
    else:
        print(f"The Goblin missed!")

                
        

print("Welcome to training! First I need to know some things about you!")
name = input("What is your name? ").strip().capitalize()

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

turn = random.randint(1,2)

while health >0 and monster_hp >0:
    if turn == 1: 
        turn = "player"
        continue
    elif turn == 2:
        turn = "monster"
        continue
    elif turn == "over":
        print("You escaped!")
        break
    elif turn == "player":
        print("Your turn!")
        user_turn(health, monster_hp, monster_defense, run, turn)
        turn = "monster"
    elif turn == "monster":
        print("The Goblin's turn!")
        monster_turn(health, defense)
        turn = "player"
else:
    if monster_hp == health:
        print("You both died!")
    elif monster_hp > health:
        print("The Goblin defeated you!")
    else:
        print("You defeated the Goblin!")