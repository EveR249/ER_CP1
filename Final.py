#ER Final CP1 2nd

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

visited = []

#def restart(stats, inventory):
def restart(stats, inventory, crowbar, keys, visited):
#While true:
    while True:
	#Would you like to restart? 
        play = input("Would you like to restart? (yes/no)").strip().lower()
	#if yes 
        if play == "yes":
		#print origin, woke up in a dungeon hall surrounded by cells with monsters and a giant bronze door. You begin to regain consciousness…
            print("You woke up in a dungeon hall surrounded by cells full of monsters. Behind you is a giant bronze door. You begin to regain consciousness...\n")

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

            #call hall function
            hallroom()
        #if no
        if play == "no":
            #print thank you for playing
            print("Thank you for playing!")
            #break
            break

#Def hall(inventory, stats)
def hallroom(inventory, stats, crowbar, keys, visited):
    if "Dungeon Hall" in visited:
        print("You have been here before")
    else:
        visited.append("Dungeon Hall")
    #While True
    while True:
        #Input option what would you like to do? 1 look around 2 open the bronze door 3 #look at the cells
        option = int(input("What would you like to do? \n1. Look around the hall \n2. Open the bronze door \n3. Look at the cells \n(Please input the number): "))

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
                           boss(inventory, stats, crowbar, keys)
                    else:
                        print("You go back to the main hall.")
                        continue
                if tool == 2:
                    print("The door won't open. You return to the hall.")
                    continue
        #Elif option is 3 then look at the cells
        elif option == 3:
            print("There are 9 cells. Each one is a different color.")
            print("Here is what you have already visited: ")
            for i in visited:
                print(i)
            choice = input("Which one would you like to open? \nRed \nOrange \nYellow \nGreen \nBlue \nIndigo \nViolet \nPink \nWhite \nBack to the dungeon hall \n (input the color or 'Hall' if you wish to return to the main dungeon hall. ").strip().lower()
            
            if choice == "red":
                redroom(inventory, stats, crowbar, keys, visited)
            if choice == "orange":
                orangeroom(inventory, stats, crowbar, keys, visited)
            if choice == "yellow":
                yellowroom(inventory, stats, crowbar, keys, visited)
            if choice == "green":
                greenroom(inventory, stats, crowbar, keys, visited)
            if choice == "blue":
                blueroom(inventory, stats, crowbar, keys, visited)
            if choice == "indigo":
                indigoroom(inventory, stats, crowbar, keys, visited)
            if choice == "violet":
                violetroom(inventory, stats, crowbar, keys, visited)
            if choice == "pink":
                pinkroom(inventory, stats, crowbar, keys, visited)
            if choice == "white":
                whiteroom(inventory, stats, crowbar, keys, visited)
            if choice == "hall":
                continue
				#If option is 10 then continue loop
				#Elif it is color, call color function

    #Return inventory, stats



#Def red room (inventory, stats)
def redroom(inventory, stats, crowbar, keys, visited):
	#Print you go over to the red cell, inside is a large and hungry goblin.
    print("You go over to the red cell, inside is a large and hungry goblin.")
    visited.append("Red Room")
	#While true
    while True:
		#Input would you like to open the cell?
        cell = input("Would you like to open the cell? (yes/no) ")
        if cell == "yes":
            if inventory == []:
                print("We can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("The monster took your crowbar!")
                    crowbar = 0
                    inventory.remove("Crowbar")
                if tool == 2:
                    print("The monster wants to fight! ")
                    combat(inventory, stats, crowbar, keys)
                    if combat(inventory, stats, crowbar, keys) == False:
                        print("You died!")
                        restart(stats, inventory)
                    else:
                        print("You defeated the monster!")
                        search = input("Do you want to search the cell? (yes/no) ")
                        if search == "yes":
                            if crowbar == 0:
                                print("You got your crowbar back!")
                                crowbar = 1
                                inventory.insert(0,"Crowbar")
                            if crowbar == 1:
                                print("There is nothing else in this room.")
                                print("You go back to the hall.")
                                hallroom(inventory, stats, crowbar, keys, visited)
                        else:
                            print("You go back to the hall.")
                            hallroom(inventory, stats, crowbar, keys, visited)
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, visited)
        return inventory, stats, crowbar, keys, visited


#Def orange room (inventory, stats)
def orangeroom(inventory, stats, crowbar, keys, visited):
    print("You go over to the orange cell, inside is a small furry creature.")
    if "Orange Room" in visited:
        print("You have been here before")
    else:
        visited.append("Orange Room")
	#While true
    while True:
        cell = input("Would you like to open the cell? (yes/no) ")
        if cell == "yes":
            if inventory == []:
                print("We can't open this yet.")
                hallroom(inventory, stats, crowbar, keys, visited)
            else:
                num = 1
                for i in inventory:
                    print(f"{num}. {i}")
                    num +=1
                tool = int(input("Which tool do you select? (input the number)"))
                if tool == 1:
                    print("The creature scratched you!")
                    stats["health"] -= 5
                if tool == 2:
                    print("The creature is scared and runs away!")
                    search = input("Do you want to search the cell? (yes/no) ")
                    if search == "yes":
                        print("You found a potion!")
                        inventory.append("Health Potion")
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, visited)
                    if search == "no":
                        print("You go back to the hall.")
                        hallroom(inventory, stats, crowbar, keys, visited)
        if cell == "no":
            print("You go back to the hall.")
            hallroom(inventory, stats, crowbar, keys, visited)
        return inventory, stats, crowbar, keys, visited


#Def yellow room (inventory, stats)
	#Print you go over to the yellow cell, inside is a giant sleeping chameleon.
	#While true
#Input would you like to open the cell?
	#If option is yes then
#Print inventory
#What do you want to use to open the cell?
#If option is crowbar then
	#Print the chameleon woke up and turned red, it's angry!!
	#The chameleon ate you!
		#Call restart function
#If option is keys then 
	#Print you opened the cell! The chameleon is still sleeping
	#Do you want to search the cell?
	#If yes then if book = no you find it
	#Add 15 to intelligence 
	#Print you go back to the hall
	#Call hall function
	
#If inventory is empty
	#print you don't have anything you can use
	#continue
#If option is no 
	#Print you return to the hall
	#Call hall function

#Return inventory, stats


#Def green room (inventory, stats)
	#Print you go over to the green cell, inside is a coughing ogre.
	#While true
#Input would you like to open the cell?
	#If option is yes then
#Print inventory
#What do you want to use to open the cell?
#If option is crowbar then
	#Print the ogre was startled, ran over to you and coughed on you!!
	#you died of airborne sickness.
		#Call restart function
#If option is keys then 
	#Print you opened the cell! The ogre puked all over the floor in terror! You become dizzy and disoriented, -5 health
	#If health is less than or = to 0 
		#Print you died!
		#Call restart function
#break
	#Do you want to search the cell?
	#If yes then you soak your shoes
	#subtract 10 from agility 
	#Print you go back to the hall
	#Call hall function
	
#If inventory is empty
	#print there is nothing you can use
	#continue
#If option is no 
	#Print you return to the hall
	#Call hall function

#Return inventory, stats

def boss():
    num = 1
    while num ==1:
        num+=1

#print welcome
#print origin, woke up in a dungeon hall surrounded by cells with monsters and a giant bronze door. You begin to regain consciousness…

#call hall function
print("You woke up in a dungeon hall surrounded by cells full of monsters. Behind you is a giant bronze door. You begin to regain consciousness...\n")
hallroom(inventory, stats, crowbar, keys, visited)

#make it so potion is always at index 2. keys are always at index 1, crowbar is always at index 0, etc so then you can make specific instances for if they choose them