#ER 2nd Lists Notes
import random

names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Eric",5 ,3.14 , False]

print(names)
print(names[3])
print(names[random.randint(1, len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names += ["Joseph", "Israel", "Zoe"]
names.remove(3.14)
x = names.index(5)
names.pop(x)
names.insert(3, "Vienna")
print(names)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(board)

board[1][1] = "X"

print(board)
#lists (changeable, ordered)
#tuple (not changeable, ordered)
classes = ("Bard", "Monk", "Barbarian", "Paladin")
#set (changeable, not ordered)
fruit = {"apple", "orange", "strawberry", "Kiwi"}
print(fruit)