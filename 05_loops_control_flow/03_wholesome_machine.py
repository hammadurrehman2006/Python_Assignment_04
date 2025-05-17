# -------------------PROBLEM STATEMENT:
'''
Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly.
'''

# default affirmation in string
affirmation = "I am constantly learning and growing, expanding my knowledge every day."

def main():
# prompt for user
    print("Please type the correct Affirmation: " + affirmation)
# input from user
    user_input = input()
# loop for correct affirmation
    while user_input != affirmation:
        print("That's not the correct affirmation.") # print when input is incorrect
# again for loop
        print("Please type the correct Affirmation: " + affirmation)
        user_input = input()
# print when its correct
    print("That's the right Affirmation.")
# calling main function
if __name__ == "__main__":
    main()