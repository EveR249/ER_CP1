#ER 2nd Order Up

#Make different dictionaries for each part of the meal (entree, drink, appetizer, side, dessert)
#inside each dictionary is 5 options and prices associated with them


def receipt(total):
    print("Here is your order:")
    print(f"Drink: {drink_choice}")
    print(f"Appetizer: {appetizer_choice}")
    print(f"Entree: {entree_choice}")
    print(f"Sides: {side_choice} and {side_choice2}")
    print(f"Dessert: {dessert_choice} \n")
    tip = float(input("How much do you want to tip (in dollars)? "))
    tax = total*.2
    total +=tax
    total +=tip
    print(f"Your total for the meal is ${total:.2f} \n")


drink = {
    "Water" : 1.25,
    "Sprite" : 1.75,
    "7-UP" : 1.65,
    "Lemon-Lime Shasta" : 1.50,
    "Sprint (Carbonated Lemon Water)" : 2.00
}

appetizer = {
    "Pretzel bites" : 5.25,
    "Cheesecake factory brown bread" : 7.00,
    "Chips and guacamole" : 4.75,
    "Caprese skewers" : 5.00,
    "Deviled eggs" : 4.50
}

entree = {
    "Grilled cheese and tomato soup" : 9.25,
    "Margherita pizza" : 10.75,
    "Vegetable masala with rice" : 10.65,
    "Mashed potatoes and gravy" : 9.50,
    "Sweet waffle with berries" : 10.00
}

side = {
    "French fries" : 1.25,
    "Waffle fries" : 1.75,
    "Curly fries" : 1.65,
    "British chips" : 1.50,
    "Smashed potatoes" : 2.00
}

dessert = {
    "Raspberry cronut" : 5.25,
    "Chocolate cake" : 6.75,
    "Pudding pie" : 7.65,
    "Donut tower" : 14.50,
    "Oreos" : 6.00
}


total = 0.0
drink_choice = 0
#print out drink options
#user input for drink, print out print, stupid proof, add price of selelction to total. 
#check if they even said something on the menu
while True:
    for key in drink:
        print(key)
    drink_choice = input("What would you like to drink? ").strip().capitalize()
    if drink_choice == "Water":
        total += drink[drink_choice]
        break
    if drink_choice == "Sprite":
        total += drink[drink_choice]
        break
    if drink_choice == "Shasta":
        total += drink["Lemon-Lime Shasta"]
        break
    if drink_choice == "7-up":
        total += drink["7-UP"]
        break
    if drink_choice == "Sprint":
        total += drink["Sprint (Carbonated Lemon Water)"]
        break
    else:
        print("We don't have that.\n")

print(f"That will bring your total to ${total}\n")

appetizer_choice = 0
#print selection for appetizer
#user input for appetizer, print out appetizer, stupid proof, add price of selelction to total. 
#check if they even said something on the menu
while True:
    for key in appetizer:
        print(key)
    appetizer_choice = input("What appetizer would you like? ").strip().capitalize()
    if appetizer_choice == "Pretzel bites":
        total += appetizer[appetizer_choice]
        break
    if appetizer_choice == "Cheesecake factory brown bread":
        total += appetizer[appetizer_choice]
        break
    if appetizer_choice == "Chips and guacamole":
        total += appetizer[appetizer_choice]
        break
    if appetizer_choice == "Caprese skewers":
        total += appetizer[appetizer_choice]
        break
    if appetizer_choice == "Deviled eggs":
        total += appetizer[appetizer_choice]
        break
    else:
        print("We don't have that.\n")

print(f"That will bring your total to ${total}\n")

#print selection for main
#user input for main, print out main, stupid proof, add price of selelction to total. 
#check if they even said something on the menu
while True:
    for key in entree:
        print(key)
    entree_choice = input("What entree would you like? ").strip().capitalize()
    if entree_choice == "Grilled cheese and tomato soup":
        total += entree[entree_choice]
        break
    if entree_choice == "Margherita pizza":
        total += entree[entree_choice]
        break
    if entree_choice == "Vegetable masala with rice":
        total += entree[entree_choice]
        break
    if entree_choice == "Mashed potatoes and gravy":
        total += entree[entree_choice]
        break
    if entree_choice == "Sweet waffle with berries":
        total += entree[entree_choice]
        break
    else:
        print("We don't have that.\n")

print(f"That will bring your total to ${total}\n")

#DONT FORGET TO DO THE 2 SIDE DISHES
#print out side options
#user input for side, print out side, stupid proof, add price of selelction to total. 
#check if they even said something on the menu
#get them to select two
while True:
    for key in side:
        print(key)
    side_choice = input("What side would you like? ").strip().capitalize()
    if side_choice == "French fries":
        total += side[side_choice]
        break
    if side_choice == "Waffle fries":
        total += side[side_choice]
        break
    if side_choice == "Curly fries":
        total += side[side_choice]
        break
    if side_choice == "British chips":
        total += side[side_choice]
        break
    if side_choice == "Smashed potatoes":
        total += side[side_choice]
        break
    else:
        print("We don't have that.\n")

print(f"That will bring your total to ${total}\n")

while True:
    for key in side:
        print(key)
    side_choice2 = input("What side would you like for your second side? ").strip().capitalize()
    if side_choice2 == "French fries":
        total += side[side_choice2]
        break
    if side_choice2 == "Waffle fries":
        total += side[side_choice2]
        break
    if side_choice2 == "Curly fries":
        total += side[side_choice]
        break
    if side_choice2 == "British chips":
        total += side[side_choice2]
        break
    if side_choice2 == "Smashed potatoes":
        total += side[side_choice2]
        break
    else:
        print("We don't have that.\n")

print(f"That will bring your total to ${total}\n")

#print out dessert options
#user input for dessert, print out dessert, stupid proof, add price of selelction to total. 
#check if they even said something on the menu
while True:
    for key in dessert:
        print(key)
    dessert_choice = input("What dessert would you like? ").strip().capitalize()
    if dessert_choice == "Raspberry cronut":
        total += dessert[dessert_choice]
        break
    if dessert_choice == "Chocolate cake":
        total += dessert[dessert_choice]
        break
    if dessert_choice == "Pudding pie":
        total += dessert[dessert_choice]
        break
    if dessert_choice == "Donut tower":
        total += dessert[dessert_choice]
        break
    if dessert_choice == "Oreos":
        total += dessert[dessert_choice]
        break
    else:
        print("We don't have that.\n")

print(f"That will bring your total to ${total}\n")

#print out their receipt and total
receipt(total)