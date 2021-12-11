import random


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

    if(is_winner(user, computer)):
        print('Yay! You won!!')

    print('Oh, you lost!')

    return 0


def is_winner(user, computer):
    """a helper function to determine the winner"""
    # return True if user wins
    if((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
        return True


play()
