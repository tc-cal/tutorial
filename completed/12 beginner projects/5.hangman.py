
import random
from word_list import words #CONTANT
import math

# CONSTANTS (CAPS)
MAX_WRONG = 10
PLAYERS = {} # dictionary {} = no duplicates

class Player:
    def __init__(self, name):
        self.name = name
        self.best_score = 11
        self.previous_words= set() # attaching words used to player

# OBJECTS
class Hangman:
    def __init__(self, player, difficulty):
        self.attempts = 0
        self.guessed = set()
        self.wrong = set()
        self.word = self.getting_word(player, difficulty=difficulty) # telling program to run def getting_word
        self.game_started = True

    def getting_word(self, player, difficulty):

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

        directory = set(words) - player.previous_words # minus the words that already used from player memory
        criteria = [w for w in directory if min_len <= len(w) <= max_len]  # do something to w for each w in directory
        the_word = random.choice(criteria).lower()
        print(f"\nThe word has {len(the_word)} letters.")
        return the_word # returning the word to the game

def hangman():
    game_started = False #TODO GPT
    while not game_started: #TODO GPT
        try:
            input_player = input("\nChoose player name: ")
            if input_player in PLAYERS:
                our_player = PLAYERS[input_player] # Fetch Player dictionary
                print(f"\nPlayer {our_player.name} found, {our_player.name} best score is {our_player.best_score}")
            else:
                our_player = Player(name=input_player) # Create the Player Object
                PLAYERS[input_player] = our_player # add to dictionary
                print(f"") #TODO COMPLETE

        except ValueError:
            print("Please enter a valid option")



        try:
            input_difficulty = input("\nChoose difficulty (easy, medium, hard): ").strip().lower()
            our_game = Hangman(player=our_player, difficulty=input_difficulty)
            game_started = our_game.game_started

        except ValueError:
            print("Please enter a valid option")


    # while len(wrong) < max_wrong:
    while our_game.attempts < MAX_WRONG:
        display = "".join([l if l in our_game.guessed else "_" for l in our_game.word]) # you are creating a list ["h", "_", "l", "l", "_"] while checking against the set of (guess)
        print(f"\n{display}")
        print(f"{MAX_WRONG - our_game.attempts} tries left\n")

        if display == our_game.word:
            print(f"You guessed the word '{our_game.word}' in {our_game.attempts} tries!")
            break

        reminder = ", ".join(sorted(our_game.guessed | our_game.wrong))  # CHEATED
        if reminder: # CHEATED only prints if not empty
            print(f"Guessed letters: {reminder}")
        guess = input("Guess a letter or the word: ").strip().lower()

        if guess == our_game.word:
            print(f"You guessed the word '{our_game.word}' in {our_game.attempts} tries!")
            break
        elif len(guess) == 1 and guess.isalpha():
            if guess in our_game.word:
                our_game.guessed.add(guess)
            else:
                our_game.wrong.add(guess)
                print(f"{guess} is not in the word.")
        elif guess in our_game.guessed or guess in our_game.wrong:
            print(f"You already guessed the letter '{guess}', try again")
            continue
        else:
            print(f"{guess.upper()} is not the word, try again.")

        our_game.attempts += 1 # PLACEMENT MATTERS, end = only add after all validation, thus skipping repeats

    else:
        print(f"\nOut of our_game.attempts. \nThe word was {our_game.word.upper()}.")

    if our_game.attempts < our_player.best_score:
        print(f"") # TODO:
        our_player.best_score = our_game.attempts
    else:
        print(f"") # TODO:

    our_player.previous_words.add(our_game.word) # saving word used

    again = input("Would you like to play again? (y/n): ").strip().lower()
    if again == "y" or again == "yes":
        hangman()
    else:
        print("Thank you for playing!")

hangman() # calling the function, like hitting 'start' after coding is completed