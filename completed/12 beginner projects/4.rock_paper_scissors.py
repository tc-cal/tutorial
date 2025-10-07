
import random

def rock_paper_scissors():
    user = input("\nPlease choose Rock (R), Paper (P), Scissors (S)\
     \n or Quit (Q): ").lower().strip()

    if user == 'q':
        return 'quit' # can also return 2 values, check GPT version line 33+

    if user not in ['r', 'p', 's', 'q']:
        return 'invalid'

    computer = random.choice(["r", "p", "s"])
    print(f'Computer chose {computer.upper()}')

    if user == computer:
        return "It's a tie!"

    if is_loser(computer, user):
        return "You've lost!"

    return "You've won!"

def is_loser(opponent, player):
    # r > s, s > p, p> r
    if (opponent == 'r' and player == 's') or \
       (opponent == 's' and player == 'p') or \
       (opponent == 'p' and player == 'r'):
        return True

# ----- main loop with scoreboard -----
score = {"You've won!": 0, "It's a tie!": 0, "You've lost!": 0}

while True:
    result = rock_paper_scissors() # if returned 2 values above, would need to define via code, message or others
    if result == 'quit': # if code == 'quit'
        print("Thank you for playing") # print(message)
        break
    if result == 'invalid':
        print("Invalid input, please enter 'R', 'P', 'S' or 'Q'")
        continue
    print(result)

    # update scoreboard and show status
    score[result] += 1
    print(f"SCORE => You: {score["You've won!"]} | Computer: {score["You've lost!"]} | Ties: {score["It's a tie!"]}")

