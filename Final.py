#ER Final CP1 2nd
import random

#Stats = {health: 100
#Intelligence : 70
#Agility : 70
#Strength : 60}
stats = {"health": 100,
        "intelligence": 70,
        "agility" : 70,
        "strength" : 60}

#Inventory = []
inventory = []
crowbar = 0
keys = 0
potion = 0
book = 0
cookie = 0
monster = 0

visited = []

#def restart(stats, inventory):
def restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
#While true:
    while True:
	#Would you like to restart? 
        play = input("Would you like to restart? (yes/no) ").strip().lower()
	#if yes 
        if play == "yes":
		#print origin, woke up in a dungeon hall surrounded by cells with monsters and a giant bronze door. You begin to regain consciousness…
            print("You woke up in a dungeon hall surrounded by cells full of monsters. Behind you is a giant bronze door. You begin to regain consciousness...")

            #Stats = {health: 100
            #Intelligence : 70
            #Agility : 70
            #Strength : 60}
            stats = {"health": 100,
                     "intelligence": 70,
                     "agility" : 70,
                     "strength" : 60}

            #Inventory = {}
            inventory = []

            visited = []
            crowbar = 0
            keys = 0
            potion = 0
            book = 0
            cookie = 0
            monster = 0

            #call hall function
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        #if no
        if play == "no":
            #print thank you for playing
            print("Thank you for playing!")
            #break
            break
        break
    

#Def hall(inventory, stats)
def hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    if "Dungeon Hall" in visited:
        print()
    else:
        visited.append("Dungeon Hall")
    #While True
    while True:
        #Input option what would you like to do? 1 look around 2 open the bronze door 3 #look at the cells
        option = int(input("\nWhat would you like to do? \n1. Look around the hall \n2. Open the bronze door \n3. Look at the cells \n(Please input the number): "))

        #If option is 1 then look around and if variable for crowbar and keys is no, you see them
        if option == 1:
            #You go over and pick them up, they are now in your inventory
            if crowbar == 0 and keys == 0:
                print("You found a crowbar and a set of keys!")
                crowbar = 1
                keys = 1
                inventory.append("Crowbar")
                inventory.append("Keys")
                continue
            #Inventory add crowbar and keys
            if crowbar == 1 and keys == 1:
                print("There is nothing left in this room.")
                continue
            #Continue loop

        #Elif option is 2 then walk over to the door and print out inventory
        if option == 2:
            #If inventory is empty then print we can’t open this yet
            if inventory == []:
                print("We can't open this yet.")
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("As you open the door you hear a booming snarl...")
                    fight = input("Are you ready to fight the final boss? (yes/no) \n").strip().lower()
                    if fight == "yes":
                           boss(inventory, stats, crowbar, keys, potion, book, cookie)
                    else:
                        print("You go back to the main hall.")
                        continue
                if tool == 2:
                    print("The door won't open. You return to the hall.")
                    continue
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        #Elif option is 3 then look at the cells
        elif option == 3:
            print("\nThere are 9 cells. Each one is a different color.")
            print("Here is what you have already visited: ")
            for i in visited:
                print(i)
            choice = input("\nWhich one would you like to open? \n\nRed \nOrange \nYellow \nGreen \nBlue \nIndigo \nViolet \nPink \nWhite \nBack to the dungeon hall \n (input the color or 'Hall' if you wish to return to the main dungeon hall. ").strip().lower()
            
            if choice == "red":
                redroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "orange":
                orangeroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "yellow":
                yellowroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "green":
                greenroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "blue":
                blueroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "indigo":
                indigoroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "violet":
                violetroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "pink":
                pinkroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "white":
                whiteroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            if choice == "hall":
                continue
				#If option is 10 then continue loop
				#Elif it is color, call color function

    #Return inventory, stats



#Def red room (inventory, stats)
def redroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
	#Print you go over to the red cell, inside is a large and hungry goblin.
    if monster == 0:
        print("You go over to the red cell, inside is a large and hungry goblin.")
    if "Red Room" in visited:
        print("\nYou have been here before")
        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
    else:
        visited.append("Red Room")
	#While true
    while True:
		#Input would you like to open the cell?
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("We can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1 and crowbar ==1:
                    print("The monster took your crowbar!")
                    crowbar = 0
                    continue
                if tool == 1 and crowbar !=1:
                    print("You can't use this")
                    continue
                if tool == 2:
                    print("The monster wants to fight! ")
                    monster = 1
                    combat(inventory, stats, crowbar, potion, book, cookie, keys)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, monster, visited


#Def orange room (inventory, stats)
def orangeroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the orange cell, inside is a small furry creature.")
    if "Orange Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("Orange Room")
	#While true
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("\nThe creature scratched you!")
                    print(stats["health"])
                    stats["health"] -= 5
                    print(stats["health"])
                    continue
                if tool == 2:
                    print("The creature is scared and runs away!")
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        if potion == 0:
                            print("You found a potion!")
                            potion = 1
                            inventory.insert(2, "Health Potion")
                            print("You go back to the hall.")
                            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, monster, visited

#Def yellow room (inventory, stats)
def yellowroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the yellow cell, inside is a giant sleeping chameleon.")
    if "Yellow Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("Yellow Room")
	#While true
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("\nThe chameleon woke up and ate you!")
                    restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 2:
                    print("The chameleon is still sleeping.")
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        if book == 0:
                            print("You found a book!")
                            book = 1
                            inventory.insert(3, "Book")
                            stats["intelligence"] +=15
                            print("You go back to the hall.")
                            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, visited

#Def green room (inventory, stats)
def greenroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the green cell, inside is a sick ogre.")
    if "Green Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("Green Room")
    #While true
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("\nThe ogre coughed on you! You got sick and died.")
                    restart(stats, inventory, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 2:
                    print("The ogre puked on the floor! You become dizzy.")
                    stats["health"] -=5
                    if stats["health"] <= 0:
                        restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        print("There is nothing in this room.")
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, monster, visited
    
def blueroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the blue cell, inside is a cowardly lion.")
    if "Blue Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("Blue Room")
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("\nThe lion tells you that they hear growling from behind the bronze door in the middle of the night.")
                    continue
                if tool == 2:
                    print("The lion hides under the bed when you open the door.")
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        if cookie == 0:
                            print("You found a cookie!")
                            cookie = 1
                            inventory.insert(4, "Cookie")
                            stats["strength"] +=15
                            print("You go back to the hall.")
                            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, monster, visited
    
def indigoroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the indigo cell, inside is a slime monster.")
    if "Indigo Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("Indigo Room")
	#While true
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("\nThe monster threw slime at you!")
                    stats["health"] -= 10
                    if stats["health"] <= 0:
                        restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    else:
                        continue
                if tool == 2:
                    print("The monster turned into a puddle of goo!")
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        print("There is nothing in this room. You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, monster, visited

def violetroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the violet cell, inside is a two headed snake.")
    if "Violet Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("Violet Room")
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("\nThe snake hisses and begins a starying contest with you...")
                    print("...\n...")
                    print("You lost.")
                    restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 2:
                    print("The snake licks you!")
                    stats["strength"] +=5
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        print("There is nothing in this room")
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, monster, visited

def pinkroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the pink cell, inside is a cotton candy sheep.")
    if "Pink Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("Pink Room")
	#While true
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("\nThe sheep trampled you!")
                    stats["health"] -= 20
                    continue
                if tool == 2:
                    print("The sheep tells you that the sick ogre is rude to everyone.")
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        print("All that's in here is cotton candy.")
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, visited
    
def whiteroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited):
    print("You go over to the white cell...\nThere is nothing inside.")
    if "White Room" in visited:
        print("\nYou have been here before\n")
    else:
        visited.append("White Room")
	#While true
    while True:
        cell = input("Would you like to open the cell? (yes/no) ").strip().lower()
        if cell == "yes":
            if inventory == []:
                print("\nWe can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1 or tool == 2:
                    print("You go into the cell.")
                    search = input("Do you want to search the cell? (yes/no) ").strip().lower()
                    if search == "yes":
                        print("There is nothing in here. Just empty white walls and the faint smell of regrets.")
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
                if tool == 3:
                    print("We can't use this.")
                    continue
                if tool == 4:
                    print("We can't use this.")
                    continue
                if tool == 5:
                    print("We can't use this.")
                    continue
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        return inventory, stats, crowbar, keys, potion, book, cookie, monster, visited

def boss(inventory, stats, crowbar, keys, potion, book, cookie):
    boss_stats = {"health" : 100,
                  "intelligence" : 30,
                  "agility" : 30,
                  "strength" : 90}
    while boss_stats["health"] > 0 or stats["health"] >0:
        num = 1
        for i in inventory:
            print(f"{num}. {i}")
            num +=1
        tool = int(input("Which combat tool do you select? (input the number)"))
        if tool == 1 and crowbar == 1:
            print("You pummel the monster with your crowbar: ")
            dmg = stats["strength"] /5
            boss_stats["health"] -= dmg
            print(f"Boss health: {boss_stats["health"]}")
        if tool == 1 and crowbar != 1:
            print("You can't use this.")
            continue
        if tool == 2 and keys == 1:
            print("You stab the monster with your keys: ")
            dmg = stats["strength"] /10 + stats["agility"] /10
            boss_stats["health"] = boss_stats["health"] - dmg
            print(f"Boss health: {boss_stats["health"]}")
        if tool == 2 and keys != 1:
            print("You can't use this.")
            continue
        if tool == 3 and potion == 1:
            print("You drink a health potion +15")
            stats["health"] +=15
            potion = 0
        if tool == 3 and potion != 1:
            print("You can't use this.")
            continue
        if tool == 4 and book == 1:
            print("You whack the monster with the book:")
            dmg = stats["intelligence"] /10
            boss_stats["health"] = boss_stats["health"] - dmg
            print(f"Boss health: {boss_stats["health"]}")
        if tool == 4 and book !=1:
            print("You can't use this.")
            continue
        if tool == 5:
            print("You can't use this.")
            continue
        if boss_stats["health"] <= 0:
            print("You won the game!")
            restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        if stats["health"] <= 0:
            print("You lost the game!")
            restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        mnstr_dmg = boss_stats["strength"] /5
        print("The monster clubbed you!")
        stats["health"] = stats["health"] - mnstr_dmg
        print(f"Your health: {stats["health"]}")
        continue
        

def combat(inventory, stats, crowbar, keys, potion, book, cookie):
    enemy_stats = {"health" : 70,
                  "intelligence" : 20,
                  "agility" : 60,
                  "strength" : 50}
    while enemy_stats["health"] > 0 or stats["health"] >0:
        num = 1
        for i in inventory:
            print(f"{num}. {i}")
            num +=1
        tool = int(input("Which combat tool do you select? (input the number)"))
        if tool == 1 and crowbar == 1:
            print("You pummel the monster with your crowbar: ")
            dmg = stats["strength"]/10 +5
            enemy_stats["health"] = enemy_stats["health"] - dmg
            print(f"Enemy health: {enemy_stats["health"]}")
        if tool == 1 and crowbar != 1:
            print("You can't use this.")
            continue
        if tool == 2:
            print("You stab the monster with your keys: ")
            dmg = stats["strength"] /10 + stats["agility"] /10
            enemy_stats["health"] = enemy_stats["health"] - dmg
            print(f"Enemy health: {enemy_stats["health"]}")
        if tool == 3:
            print("You drink a health potion +15")
            stats["health"] +=15
            potion = 0
        if tool == 4:
            print("You whack the monster with the book:")
            dmg = stats["intelligence"] /10
            enemy_stats["health"] = enemy_stats["health"] - dmg
            print(f"Enemy health: {enemy_stats["health"]}")
        if tool == 5:
            print("You can't use this.")
            continue
        if enemy_stats["health"] <= 0:
            print("You defeated the monster!")
            if crowbar == 0:
                print("You got your crowbar back!")
                crowbar = 1
            if crowbar == 1:
                print("There is nothing else in this room.")
                print("You go back to the hall.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
            else:
                print("You go back to the hall.")
                hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        if stats["health"] <= 0:
            print("You lost the game!")
            restart(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)
        mnstr_dmg = enemy_stats["strength"] /5
        print("The monster clubbed you!")
        stats["health"] = stats["health"] - mnstr_dmg
        print(f"Your health: {stats["health"]}")
        continue

#print welcome
#print origin, woke up in a dungeon hall surrounded by cells with monsters and a giant bronze door. You begin to regain consciousness…

#call hall function
while True:
    print("You woke up in a dungeon hall surrounded by cells full of monsters. Behind you is a giant bronze door. You begin to regain consciousness...")
    hallroom(inventory, stats, crowbar, keys, potion, book, cookie, monster, visited)

#make it so potion is always at index 2. keys are always at index 1, crowbar is always at index 0, etc so then you can make specific instances for if they choose them