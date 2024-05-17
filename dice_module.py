import random

def roll_dice():
    """
    Rolls three dice and returns their values as a tuple.

    Returns:
        tuple: A tuple containing the values of the three rolled dice.
    """    
    die1 = random.randint(1, 6) 
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    return die1, die2, die3