# Import the random module to generate random numbers
import random 

def main():
# Generate a random number between 1 and 15 and store it in the variable `real_number`
    real_number = random.randint(0, 99)
# Infinite loop to keep the game running until the user guesses the correct number
    while True:
# Prompt the user to guess the number, and convert the input to an integer
        guessed_number = int(input("Guess the number (between 0 and 99): "))
# Check if the guessed number is lower than the real number
        if (real_number > guessed_number):
            print("Your guess is low.")    
# Check if the guessed number is higher than the real number
        elif (real_number < guessed_number):
            print("Your guess is high.")
# If the guessed number matches the real number, break the loop
        else:
            print("Congratulations! You guessed the correct number.")
            break  # Exit the loop when the correct number is guessed

if __name__ == "__main__":
    main()