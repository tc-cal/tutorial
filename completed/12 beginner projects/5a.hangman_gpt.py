import random

def hangman():
    # Step 1: Choose difficulty
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
        if difficulty == "easy" or difficulty == "e": # able to narrow it down to 2 due to .strip() which strips spaces & lines and .lower()
            min_len, max_len = 2, 3
            break
        elif difficulty == "medium" or difficulty == "m":
            min_len, max_len = 4, 5
            break
        elif difficulty == "hard" or difficulty == "h":
            min_len, max_len = 6, 100   # "6 or more"
            break
        else:
            print("Please enter 'easy', 'medium', or 'hard'.")

    # Step 2: Pick a word from dictionary based on difficulty
    directory = ["hi", "hey", "heyo", "hello", "heyhey"]
    valid_words = [w for w in directory if min_len <= len(w) <= max_len]
    word = random.choice(valid_words)

    # Step 3: Initialize game state
    guessed_letters = set()
    attempts = 0
    max_attempts = 10  # tweakable

    print(f"\nYour word has {len(word)} letters.")

    # Step 4: Game loop
    while attempts < max_attempts:
        # Display word with guessed letters filled in
        display = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print("Word: " + display)

        # Win check
        if display == word:
            print(f"🎉 You guessed the word '{word}' in {attempts} tries!")
            break

        guess = input("Guess a letter or the whole word: ").lower().strip()
        attempts += 1

        # Whole word guess
        if guess == word:
            print(f"🎉 You guessed the word '{word}' in {attempts} tries!")
            break
        # Single letter guess
        elif len(guess) == 1 and guess.isalpha():
            if guess in word:
                guessed_letters.add(guess)
                print(f"✅ Good guess: {guess}")
            else:
                print(f"❌ {guess} is not in the word.")
        else:
            print("Please enter a single letter or guess the full word.")

    else:  # runs if loop ends without a break
        print(f"😢 Out of attempts! The word was '{word}'.")

hangman()
