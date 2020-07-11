#  A simple guessing game.

# TODO:  get player name 
    # get random number - secret number
    # get player guesses
    #       give hint after 3 tries
    # display result after 5 tries
    # decompose the program

import random as r

lower_limit = r.randint(0, 40)
upper_limit = r.randint(60, 100)
com_guess = r.randint(lower_limit, upper_limit)

print(f"DEBUG: com guess = {com_guess}")

player_name = input("Hey! What's your name: ").capitalize()
print(f"\n{player_name}! I am thinking of a number between {lower_limit} and {upper_limit}")

for guesses in range(1, 6):
    
    guess = int(input("Make a Guess: "))
    if guess > upper_limit or guess < lower_limit:
        print(f"\nOh! common, {guess} is not in the range {lower_limit}-{upper_limit}.")
    elif guess < com_guess:
        print("\nYour Guess is too low! Guess higher")

        # FIXME - Hint - FIXED
        if guesses > 3:
            print(f"Hint: the difference between {guess} and my number is {com_guess - guess}\n")
    elif guess > com_guess:
        print("\nYour Guess is too high! Guess lower.")

        # FIXME - Hint - FIXED
        if guesses > 3:
            print(f"Hint: the difference between {guess} and my number is {guess - com_guess}\n")
    else:
        break

# try_time = "tries" if guesses > 1 else "try\nyou are very lucky"
try_time = ("tries", "try.\nYou are a very lucky person.") [guesses == 1] 

if guess == com_guess:
    print(f"\nCongrats! {player_name}, You guessed my number in {guesses} {try_time}.")
else:
    print(f"\nSorry! {player_name}, the number I was thinking is {com_guess}.")
