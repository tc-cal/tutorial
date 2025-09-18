
import random
from word_list import words
import math

def hangman():
    while True:
        try:
            difficulty = input("\nchoose difficulty (easy, medium, hard): ").strip().lower()
            if difficulty == "easy" or difficulty == "e":
                min_len, max_len = 1, 4
                print("Your word will be 1 to 4 letters long")
            elif difficulty == "medium" or difficulty == "m":
                min_len, max_len = 5, 6
                print("Your word will be 5 or 6 letters long")
            elif difficulty == "hard" or difficulty == "h":
                min_len, max_len = 7, 100
                print("Your word will be 7 or more letters long")
            else:
                raise ValueError("Please enter a valid difficulty")
            break
        except ValueError:
            print("Please enter a valid option")

    directory = words # can + words at the end
    criteria = [w for w in directory if min_len <= len(w) <= max_len] # do something to w for each w in directory
    the_word = random.choice(criteria).lower()

    attempts = 0
    limit = 15
    max_attempts = min(limit, math.ceil(1.5 * len(the_word)))
    max_wrong = 10 # alternative
    guessed = set()
    wrong = set()

    print(f"\nThe word has {len(the_word)} letters.")

    # while len(wrong) < max_wrong:
    while attempts < max_attempts:
        display = "".join([l if l in guessed else "_" for l in the_word]) # you are creating a list ["h", "_", "l", "l", "_"] while checking against the set of (guess)
        print(f"\n{display}")
        print(f"{max_attempts - attempts} tries left\n")

        if display == the_word:
            print(f"You guessed the word '{the_word}' in {attempts} tries!")
            break

        reminder = ", ".join(sorted(guessed | wrong))  # CHEATED
        if reminder: # CHEATED only prints if not empty
            print(f"Guessed letters: {reminder}")
        guess = input("Guess a letter or the word: ").strip().lower()

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

        attempts += 1 # PLACEMENT MATTERS, end = only add after all validation, thus skipping repeats

    else:
        print(f"\nOut of attempts. \nThe word was {the_word.upper()}.")
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again == "y" or again == "yes":
            hangman()
        else:
            print("Thank you for playing!")

hangman() # calling the function, like hitting 'start' after coding is completed