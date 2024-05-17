# tuple out dice game main script

import os
import random

from dice_module import roll_dice # Imports the roll_dice function from the module

print("Welcome to my Dice Game!")

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
    total_turns = 0 # Keeps track of the total number of turns
    current_turn = 1    

    player_scores = [0] * num_players

    # The game loop
    while True:
        print(f"\nTurn {current_turn}")
        for player in range(num_players):
            print(f"\nPlayer {player+1}'s turn:")
            player_scores[player] += play_turn()
            print(f"Player {player+1}'s score: {player_scores[player]}")
    
            # Check if the player has reached the target score
            if player_scores[player] >= target_score:
                print(f"\nPlayer {player+1} wins!")
                return

        # Increment the current turn after all players have gone once
        current_turn += 1
        total_turns += 1  # Increment the total number of turns

        # Check if the total number of turns has reached 5
        if total_turns >= 5:
            break
    
    # Determines the winner if the target score wasn't reached
    max_score = max(player_scores)
    winners = [player + 1 for player, score in enumerate(player_scores) if score == max_score]
    if len(winners) == 1:
        print(f"\nPlayer {winners[0]} wins with a score of {max_score}!")
    else:
        print(f"\nIt's a tie! Players {', '.join(map(str, winners))} have the highest score of {max_score}.")

# Start the game
while True: # Continuously calls 'play_game' until the players choose not to play again
    play_game()
    
    # Prompt players if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break