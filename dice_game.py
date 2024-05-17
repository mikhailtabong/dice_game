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
        
        # Check for fixed dice
        for die in dice:
            if dice.count(die) == 2 and die not in fixed_dice:
                fixed_dice.append(die)
        
        # Calculate the score for the current roll
        score = sum(dice)

        # Ask the player if they want to roll again
        if len(fixed_dice) < 3:
            choice = input("Roll again? (y/n): ")
            if choice.lower() != 'y':
                break
        else:
            break

    print(f"Turn ends with a score of {score} points.")
    return score

# main game loop :D
def play_game():
    num_players = int(input("Enter the number of players: "))
    target_score = int(input("Enter the target score to reach: "))

    player_scores = [0] * num_players

    # The game loop
    while True:
        for player in range(num_players):
            print(f"\nPlayer {player+1}'s turn:")
            player_scores[player] += play_turn()
            print(f"Player {player+1}'s score: {player_scores[player]}")
            return
    
    # Check if the player has reached the target score
            if player_scores[player] >= target_score:
                print(f"\nPlayer {player+1} wins!")
                return

# Start the game
play_game()
    