
import random
def play():
    user = input("\nWhat's your choice 'R' for rock, 'P' for paper, 'S' for scissors, or 'Q' to quit game: ").lower().strip()

    if user == 'q':
        return "quit" # special flag

    if user not in ['r', 'p', 's']:
        return"Invalid input. please enter 'R', 'P' or 'S'."

    computer = random.choice(['r', 'p', 's'])
    print(f'Computer chose {computer.upper()}')

    if user == computer:
        return 'It\'s a tie'

    if is_winner(user, computer):
        return 'You won'

    return 'You lost'

def is_winner(player, opponent):
    # r > s, s > p, p> r
    if (player == 'r' and opponent == 's') or \
        (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True

# TODO add score keeping
# TODO figure out how does the code know what 'result' is to be printed, where was it defined or linked to the returning
# TODO rather, explain the code to me line by line like I'm 5

while True:
    result = play()
    if result == 'quit':
        print("Thank you for playing!")
        break
    print(result)


