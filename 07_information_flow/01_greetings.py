# ---------------------PROBLEM STATEMENT:
'''
We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.
'''

# Function to greet the user by their name
def greet(user_name):
# Concatenate the greeting message with the user's name
    return "Greetings " + user_name + "!"  # Return the full greeting message

def main():
# Prompt the user to enter their name and store it in the variable 'user_name'
    user_name = input("What's your name? ")  
# Call the greet function and print the greeting
    print(greet(user_name))  # Display the greeting message to the user

# Call main function
if __name__ == '__main__':
    main()
