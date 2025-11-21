import random

def roulette_like_trial(p_win=0.49):
    """
    Returns True if the bettor wins (probability p_win),
    otherwise returns False.
    """
    return random.random() < p_win
