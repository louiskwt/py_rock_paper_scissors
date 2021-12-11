def is_winner(user, computer):
    """a helper function to determine the winner"""
    # return True if user wins
    if((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
        return True
