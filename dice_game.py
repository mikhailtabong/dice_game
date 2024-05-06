# tuple out dice game main script

import os
import random

print("Welcome to my Dice Game!")

# Function to roll the dice
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    return die1, die2, die3

# Function to play a turn
def play_turn():
    fixed_dice = []
    score = 0

    while True:
        # Roll the dice
        dice = roll_dice()
        print(f"Dice rolled: {dice}")
        
        # Check if all three dice are the same (tuple out)
        if dice[0] == dice[1] == dice[2]:
            print("Tuple out! Turn ends with 0 points.")
            return 0
        
        # Calculate the score for the current roll
        score = sum(dice)