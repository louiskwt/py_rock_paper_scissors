import random
from helper import is_winner


def play():
    """The play function represent the game logic"""
    user = input(
        "type 'r' for rock, 'p' for paper, or 's' for scissors:  ")  # ask the user for input
    # the computer picks a random input
    computer = random.choice(['r', 'p', 's'])

    print(f"Computer: {computer} |  You: {user}")
    # Come up the rules to determine who wins
    # Draw
    if(user == computer):
        print('tie')
        return 0

    if(is_winner(user, computer)):
        print('Yay! You won!!')
    else:
        print('Oh, you lost!')

    return 0


play()
