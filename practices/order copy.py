#ER 2nd Order Up

#Make different dictionaries for each part of the meal (entree, drink, appetizer, side, dessert)
#inside each dictionary is 5 options and prices associated with them


menu = {
    "drinks" : {
        "Water" : 1.25,
        "Sprite" : 1.75,
        "7-UP" : 1.65,
        "Lemon-Lime Shasta" : 1.50,
        "Sprint (Carbonated Lemon Water)" : 2.00
    },

    "appetizers" : {
        "Pretzel bites" : 5.25,
        "Cheesecake factory brown bread" : 7.00,
        "Chips and guacamole" : 4.75,
        "Caprese skewers" : 5.00,
        "Deviled eggs" : 4.50
    },

    "entrees" : {
        "Grilled cheese and tomato soup" : 9.25,
        "Margherita pizza" : 10.75,
        "Vegetable masala with rice" : 10.65,
        "Mashed potatoes and gravy" : 9.50,
        "Sweet waffle with berries" : 10.00
    },

    "sides" : {
        "French fries" : 1.25,
        "Waffle fries" : 1.75,
        "Curly fries" : 1.65,
        "British chips" : 1.50,
        "Smashed potatoes" : 2.00
    },

    "desserts" : {
        "Raspberry cronut" : 5.25,
        "Chocolate cake" : 6.75,
        "Pudding pie" : 7.65,
        "Donut tower" : 14.50,
        "Oreos" : 6.00
    }
}

def order(total):
    for key in menu["drinks"]:
        print(key)
    while True:
        user_drink = input("What drink would you like?: ").strip().capitalize()
        if user_drink in menu["drinks"].keys():
            total += menu["drinks"][user_drink]
            print()
            break
        else:
            print("Try again. ")
    for key in menu["appetizers"]:
        print(key)
    while True:
        user_appetizer = input("What appetizer would you like?: ").strip().capitalize()
        if user_appetizer in menu["appetizers"].keys():
            total += menu["appetizers"][user_appetizer]
            print()
            break
        else:
            print("Try again. ")
    for key in menu["entrees"]:
        print(key)
    while True:
        user_entree = input("What entree would you like?: ").strip().capitalize()
        if user_entree in menu["entrees"].keys():
            total += menu["entrees"][user_entree]
            print()
            break
        else:
            print("Try again. ")
    for key in menu["sides"]:
        print(key)
    while True:
        user_side = input("What side would you like for your first side?: ").strip().capitalize()
        if user_side in menu["sides"].keys():
            total += menu["sides"][user_side]
            print()
            break
        else:
            print("Try again. ")
    while True:
        user_side2 = input("What other side would you like?: ").strip().capitalize()
        if user_side2 in menu["sides"].keys():
            total += menu["sides"][user_side2]
            print()
            break
        else:
            print("Try again. ")
    for key in menu["desserts"]:
        print(key)
    while True:
        user_dessert = input("What dessert would you like?: ").strip().capitalize()
        if user_dessert in menu["desserts"].keys():
            total += menu["desserts"][user_dessert]
            print()
            break
        else:
            print("Try again. ")
    print("Here is your order:")
    print(f"Drink: {user_drink}")
    print(f"Appetizer: {user_appetizer}")
    print(f"Entree: {user_entree}")
    print(f"Sides: {user_side} and {user_side2}")
    print(f"Dessert: {user_dessert} \n")
    tip = float(input("How much do you want to tip (in dollars)? "))
    tax = total*.2
    total +=tax
    total +=tip
    print(f"Your total for the meal is ${total:.2f} \n")
    

total = 0.0

order(total)