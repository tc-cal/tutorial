
import random
from word_list import words
import string

def hangman():
    while True:
        try:
            difficulty = input("choose difficulty (easy, medium, hard): ").strip().lower()
            if difficulty == "easy" or difficulty == "e":
                min_len, max_len = 1, 3
                print("Your word will be 1 to 3 letters long")
            elif difficulty == "medium" or difficulty == "m":
                min_len, max_len = 4, 5
                print("Your word will be 4 or 5 letters long")
            elif difficulty == "hard" or difficulty == "h":
                min_len, max_len = 6, 100
                print("Your word will be 6 or more letters long")
            break
        except ValueError:
            print("Please enter a valid option")

    directory = words # can + words at the end
    criteria = [w for w in directory if min_len <= len(w) <= max_len] # do something to w for each w in directory
    the_word = random.choice(criteria)

    attempts = 0
    max_attempts = 10
    guessed = set()

    print(f"\nThe word has {len(the_word)} letters.")

    while attempts < max_attempts:
        display = "".join([l if l in guessed else "_" for l in the_word]) # you are creating a list ["h", "_", "l", "l", "_"] while checking against the set of (guess)
        print(f"Word: {display}")

        if display == the_word:
            print(f"You guessed the word '{the_word}' in {attempts} tries!")
            break

        guess = input("Guess a letter: ").strip().lower()
        attempts += 1

        if guess in the_word:
            guessed.add(guess)
            print(f"Good guess: {guess}")
        else:
            print(f"{guess} is not in the word.")
    else:
        print(f"\n Out of attempts. \n The word was {the_word}.")

hangman() # calling the function, like hitting 'start' after coding is completed