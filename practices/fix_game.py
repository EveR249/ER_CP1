#ER 2nd Fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #guess = input("Enter your guess: ") this needs to be converted to an integer so it can be used properly and be compared to the number. if its not an integer you can't use comparison operators. I replaced with the code below. Run time error
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        #if guess == number_to_guess:
            #print("Congratulations! You've guessed the number!")
            #game_over = True
            #I moved this to be below the other statements and changed it to be an elif. this is so it won't print too low or too high AFTER it says you ran out of attempts. Logic error
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts +=1 #have to add this so they don't have unlimited attempts. logic error
        elif guess < number_to_guess:
            print("Too low! Try again.")
            attempts +=1  #have to add this so they don't have unlimited attempts. logic error
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        #continue
        # you don't need this one it doesn't change anything. Logic
    print("Game Over. Thanks for playing!")
start_game()