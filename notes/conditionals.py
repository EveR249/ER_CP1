#ER 2nd Conditionals notes
import random

#num = float(input("Enter a number: "))

#if num >0:
    #print(f"the number {num} is positive")
#elif num <0:
    #print(f"the number {num} is negative")
#else:
    #print(f"the number {num} is zero")

monster_hp = 30
dmg_modifier = 2
atk_bonus = 3
player_hp = 25

roll = random.randint(1,20)

if roll ==20:
    print("You rolled a critical hit! Double your damage")
    attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster! It now has {monster_hp} health!")
elif roll+atk_bonus > 10:
    print("You hit!")
    attack = random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster! It now has {monster_hp} health!")
elif roll <= 10:
    if roll == 1:
        print(f"The monster attacked you!")
        damage = (random.randint(1,10) +2)
        player_hp -= damage
        print(f"You took {damage} damage! You now have {player_hp}")
    else:
        print("You missed.")
else:
    print("That shouldn't be possible.")

print("Your turn is over.")


if monster_hp and monster_hp > 0:
    print("It is the monsters turn.")
else:
    print("The monster is dead.")