
import random

def play():
    user = input("\nChoice 'R' for rock, 'P' for paper, 'S' for scissors "
                 "or 'Q' to quit: ").lower().strip()

    if user == 'q':
        return 'quit', "Thank you for playing!"         # signal quit + message

    if user not in ['r', 'p', 's']:
        return 'invalid', "Invalid input. Please enter R, P, S or Q."

    computer = random.choice(['r', 'p', 's'])
    print(f'Computer chose {computer.upper()}')          # OK to print inside

    if user == computer:
        return 'tie', "It's a tie"

    if is_winner(user, computer):
        return 'win', "You won"

    return 'loss', "You lost"

def is_winner(player, opponent):
    return ((player == 'r' and opponent == 's') or
            (player == 's' and opponent == 'p') or
            (player == 'p' and opponent == 'r'))

# ----- main loop with scoreboard -----
scores = {'win': 0, 'loss': 0, 'tie': 0}

while True:
    code, message = play()          # call play(), get result code + message
    if code == 'quit':
        print(message)
        break
    if code == 'invalid':
        print(message)
        continue                    # don't change scores for invalid tries

    # update scoreboard and show status
    scores[code] += 1
    print(message)
    print(f"Score -> You: {scores['win']} | Comp: {scores['loss']} | Ties: {scores['tie']}")
