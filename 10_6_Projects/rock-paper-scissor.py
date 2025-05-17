import random

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play():
# user input choice
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    
# input choice with validation
    while user not in ['r', 'p', 's']:
        user = input("Invalid input. Please enter 'r' for rock, 'p' for paper, or 's' for scissor: ")

# Computer's random choice
    computer = random.choice(['r', 'p', 's'])

# Display
    print(f"Computer chose: {computer}")

# It's a tie when both choose the 
    if user == computer:
        return "It's a tie!"

# You win when the user's choice beats the computer's choice
    if is_win(user, computer):
        return 'You win!'

# If the player loses the game
    return 'You lost!'

# Start the game and print the result of the round
print(play())
