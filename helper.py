def is_winner(user, computer):
    """a helper function to determine the winner"""
    # return True if user wins
    if((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
        return True


def is_wrong_input(user):
    """a helper function to determine the winner"""
    # return True is user enter something besides 'r' / 'p' / 's'
    if(user != 'r' or user != 'p' or user != 's'):
        return True
