# Tuple Out Dice Game Consolidation Project

This Python program implements a simple dice game called "Tuple Out". The game follows these rules:

    1. One or more players take turns rolling three dice to score points.
    2. If all three dice show the same number, the player "tuples out" and scores 0 points for that turn.
    3. If two dice have the same value, they are "fixed" and cannot be re-rolled.
    4. The player can choose to re-roll any non-fixed dice until they decide to stop or "tuple out".
    5. When a player stops rolling, they score points equal to the sum of the three dice.
    6. The game continues until a player reaches a predetermined target score.

The code is structured into three main functions:
    roll_dice(): Rolls three dice by generating random numbers between 1 and 6
    play_turn(): Single turn for a player, handling dice rolls, fixed dice, and scoring
    play_game(): Manages the overall game flow, including the player turns and determining the winner
