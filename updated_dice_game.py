import random

# Function to simulate rolling three dice
def roll_dice():
    return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

print("Welcome to my Dice Game!")

# Function to play a turn
def play_turn(player_num):
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

    print(f"Player {player_num}'s turn ends with a score of {score} points.")
    return score

# Main game function
def play_game():
    num_players = int(input("Enter the number of players: "))
    target_score = int(input("Enter the target score to reach: "))

    player_scores = [0] * num_players

    # Each player takes a turn
    for player_num in range(1, num_players + 1):
        print(f"\nPlayer {player_num}'s turn:")
        player_scores[player_num - 1] += play_turn(player_num)
        print(f"Player {player_num}'s total score: {player_scores[player_num - 1]}")

    # Determine the winner
    max_score = max(player_scores)
    winners = [i + 1 for i, score in enumerate(player_scores) if score == max_score]
    if len(winners) == 1:
        print(f"\nPlayer {winners[0]} wins with a score of {max_score}!")
    else:
        print(f"\nIt's a tie! Players {', '.join(map(str, winners))} have the highest score of {max_score}.")

# Start the game
while True:
    play_game()
    
    # Prompt players if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break
