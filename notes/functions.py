#ER 2nd functions notes

num = 0
player_hp = 100
monster_hp = 100

def add(x,y):
    return x+y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp-dmg, 

while num <add(5,5):
    print("Duck")
    num +=1
print("Goose")
print(f"results are {add(6,89)}")
total = add(6,89)
print(add(add(3.14,.85), 10))
add(6,89)
add(7,5)
add(59,7)
add(95,5)
add(45,8)

print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Eve's initials are: {initials("Eve E Richardson")}")

monster_hp, player_hp = attack(15, "monster")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")