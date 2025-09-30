#ER 2nd Shopping list manager

shopping_list = ["Shopping List:"]
print("Lets create a shopping list!")

while True:
    action = input("What would you like to do? (Add, remove, view, or exit) ").strip().lower()
    if action == "add":
        item = input("What item do you want to add to the list? ").capitalize().strip()
        shopping_list.append(item)
    elif action == "remove":
        for x in shopping_list:
            print(x)
        item = input("What item on the list do you want to remove? ").strip().capitalize()
        shopping_list.remove(item)
    elif action == "view":
        for x in shopping_list:
            print(x)
    elif action == "exit":
        print("Thank you for using this program!")
        break