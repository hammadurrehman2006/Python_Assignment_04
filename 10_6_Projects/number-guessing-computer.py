# Import the random module to generate random numbers
import random 

# Generate a random number between 1 and 15 and store it in the variable `real_number`
real_number = random.randint(1, 15)

# Infinite loop to keep the game running until the user guesses the correct number
while True:
    # Prompt the user to guess the number, and convert the input to an integer
    guessed_number = int(input("Guess the number (between 1 and 15): "))

    # Check if the guessed number is lower than the real number
    if (real_number > guessed_number):
        print("Your guessed number is lower than the real number.")
    
    # Check if the guessed number is higher than the real number
    elif (real_number < guessed_number):
        print("Your guessed number is higher than the real number.")
    
    # If the guessed number matches the real number, break the loop
    else:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop when the correct number is guessed

