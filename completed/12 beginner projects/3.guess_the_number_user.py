
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low, try again')
        elif guess > random_number:
            print('Too high, try again')

    print(f'You guessed {guess} correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':  # loop until user says correct
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c/ low = high

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower().strip()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f'Computer guessed {guess} correctly')
        else:
            print("Invalid input. please enter 'H', 'L', or 'C'.")



computer_guess(10)