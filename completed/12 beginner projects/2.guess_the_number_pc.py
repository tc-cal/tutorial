
import random

def guess(): # can also write as simple inline code without def, would not need :
    while True: # runs infinite loop until 'break' vs while x != y runs til x == y
        try:
            x = int(input("Set the maximum number (eg. 100): "))
            if x < 1:
                print("Please enter a number greater than 1")
                continue
            break
        except ValueError: # runs this instead of crashing if the 'try' above doesn't work
            print("Please enter a valid whole number")

    random_number = random.randint(1, x) # refers to the max 'x' set in prev loop
    guess = 0 # can also uses 'none', as long as != random_number
    attempts = 0
    max_attempts = 10
    while guess != random_number and attempts < max_attempts:
        guess = int(input(f'Guess a number between 1 and {x}: '))

        attempts += 1

        if guess < 1 or guess > x:
            print(f'Stay within 1-{x}: ')
        elif guess > random_number:
            print(f'Too high, try again! (attempt {attempts}/{max_attempts}: )')
        elif guess < random_number:
            print(f'Too low, try again! (attempt {attempts}/{max_attempts}: )')
    print(f'You guessed the number "{random_number}" in {attempts} tries!')


while True:
    guess()
    again = input("Would you like to play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thank you for playing!")
        break

'guess(100)' # this line has been replaced by user input at beginning, no longer needed

    # guesses = 0
    # while guesses != x:
    #     guesses += 1
    #     if guesses > x:
    #         print("Too high")
    #