#ER 2nd User Sign in

user1 = "dog"
user2 = "cat"
user3 = "bird"
user4 = "bunny"
user5 = "lizard"

pass1 = "doggies"
pass2 = "kitties"
pass3 = "tweet"
pass4 = "bunnies"
pass5 = "gecko"

username = input("What is your username? ").strip()
password = input("What is your password? ")


if username == user1:
    if password == pass1:
        print("Welcome!")
    else:
        print("Invalid username or password")
elif username == user2:
    if password == pass2:
        print("Welcome!")
    else:
        print("Invalid username or password")
elif username == user3:
    if password == pass3:
        print("Welcome!")
    else:
        print("Invalid username or password")
elif username == user4:
    if password == pass4:
        print("Welcome!")
    else:
        print("Invalid username or password")
elif username == user5:
    if password == pass5:
        print("Welcome!")
    else:
        print("Invalid username or password")
else:
    print("Please double check your information is correct, you may also not be in our system yet.")