#ER 2nd RANDOM NUMBERS NOTES
import random

# examples of random numbers
print(random.random()) #float between 0 and 1
print(random.randint(1,6)) 


name = input("what is your name? ").strip().title()

# Random stat creator D&D
stat_one = random.randint(1,10)+random.randint(1,10)
stat_two = random.randint(1,10)+random.randint(1,10)
stat_three = random.randint(1,10)+random.randint(1,10)
stat_four = random.randint(1,10)+random.randint(1,10)
stat_five = random.randint(1,10)+random.randint(1,10)
stat_six = random.randint(1,10)+random.randint(1,10)
stat_seven = random.randint(1,10)+random.randint(1,10)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

strength = int(input("Which stat are you picking for strength? ")) + 2