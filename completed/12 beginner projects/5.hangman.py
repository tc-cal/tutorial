
import random
from word_list import words
import math

def hangman():
    while True:
        try:
            difficulty = input("\nchoose difficulty (easy, medium, hard): ").strip().lower()
            if difficulty == "easy" or difficulty == "e":
                min_len, max_len = 1, 4
                print("Your word will be 1 to 3 letters long")
            elif difficulty == "medium" or difficulty == "m":
                min_len, max_len = 5, 6
                print("Your word will be 4 or 5 letters long")
            elif difficulty == "hard" or difficulty == "h":
                min_len, max_len = 7, 100
                print("Your word will be 6 or more letters long")
            else:
                raise ValueError("Please enter a valid difficulty")
            break
        except ValueError:
            print("Please enter a valid option")

    directory = words # can + words at the end
    criteria = [w for w in directory if min_len <= len(w) <= max_len] # do something to w for each w in directory
    the_word = random.choice(criteria).lower()

    attempts = 0
    limit = 12
    max_attempts = min(limit, math.ceil(1.5 * len(the_word)))
    guessed = set()
    wrong = set()

    print(f"\nThe word has {len(the_word)} letters.")

    while attempts < max_attempts:
        display = "".join([l if l in guessed else "_" for l in the_word]) # you are creating a list ["h", "_", "l", "l", "_"] while checking against the set of (guess)
        print(f"\n{display}")
        print(f"{max_attempts - attempts} tries left\n")

        if display == the_word:
            print(f"You guessed the word '{the_word}' in {attempts} tries!")
            break

#TODO separate out word & letter guesses, change word guess to display 'incorrect word'
        reminder = ", ".join(sorted(guessed | wrong))  # CHEATED
        print(f"Guessed letters: {reminder}")
        guess = input("Guess a letter or the word: ").strip().lower()
        attempts += 1

        if guess == the_word:
            print(f"You guessed the word '{the_word}' in {attempts} tries!")
            break
        elif len(guess) == 1 and guess.isalpha():
            if guess in the_word:
                guessed.add(guess)
            else:
                wrong.add(guess)
                print(f"{guess} is not in the word.")
        elif guess in guessed or guess in wrong:
            print(f"You already guessed the letter '{guess}', try again")
            continue
        else:
            print(f"{guess.upper()} is not the word, try again.")

    else:
        print(f"\nOut of attempts. \nThe word was {the_word.upper()}.")
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again == "y":
            hangman()
        else:
            print("Thank you for playing!")

hangman() # calling the function, like hitting 'start' after coding is completed