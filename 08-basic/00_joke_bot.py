# Define the constants
USER_PROMPT = "What do you want? "
FUNNY_JOKE = "Here is a joke for you! ====== Why do programmers prefer dark mode? Because the light attracts bugs!======="
JOKE_ONLY = "Sorry I only tell jokes."

def main():
# Ask the user for input
    user_choice = input(USER_PROMPT).strip()  # Get the user input and remove any extra spaces

# Respond based on what the user types
    if user_choice == "joke":
        print(FUNNY_JOKE)  # If the user says "Joke", print the new joke
    else:
        print(JOKE_ONLY)  # If the user says anything else, print the sorry message

if __name__ == '__main__':
    main()
