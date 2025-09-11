
import random
from word_list import words
import string

def hangman():
    while True:
        try:
            difficulty = input("choose difficulty (eg. easy, medium, hard): ").strip().lower()
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

    directory = words
    choices = (w for w in directory if min_len <= len(directory) <= max_len)
    the_word = random.choice(choices)
    attempts = 0
    max_attempts = 10
    guessed = []
    display = "".join(l if l in guessed else "_" for l in the_word)
    print(f"Word: {display}")

    while attempts < max_attempts:
        if display == word:
            print(f"🎉 You guessed the word '{word}' in {attempts} tries!")
            break

        guess = input("Guess a letter: ")
        attempts += 1

        if guess in the_word:
            guessed.add(guess)
            print(f"Good guess: {guess}")
        else:
            print(f"{guess} is not in the word.")
