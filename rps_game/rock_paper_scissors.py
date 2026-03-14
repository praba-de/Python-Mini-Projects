# Rock Paper Scissors Game
# This program lets a user play Rock, Paper, Scissors against the computer

import random

# Initialize win counters
user_wins = 0
computer_wins = 0

# Available options
options = ["rock", "paper", "scissors"]

# Game loop
while True:
    # Ask the user for input
    user_input = input("Type rock/paper/scissors OR q to quit: ").lower()

    # Exit the game
    if user_input == "q":
        break

    # Check if the input is valid
    if user_input not in options:
        continue

    # Computer randomly chooses an option
    random_num = random.randint(0, 2)
    computer_picked = options[random_num]
    print("Computer picked", computer_picked)

    # Check winning conditions
    if user_input == "rock" and computer_picked == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_picked == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_picked == "rock":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

# Display final results
print("You won", user_wins, "times!")
print("Computer won", computer_wins, "times!")
print("Goodbye!")