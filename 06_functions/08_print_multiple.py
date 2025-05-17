# -------------------PROBLEM STATEMENT:
'''
Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.
'''

# Function to print a message multiple times
def repeat_message(text: str, times: int):
# Loop for 'times' number of times
    for _ in range(times): 
        print(text)

def main():
# Prompt user for a message
    text = input("Please type a message: ")
 # Prompt user for the number of repetitions
    times = int(input("Enter a number of times to repeat your message: ")) 
# Call the repeat_message function with text and times
    repeat_message(text, times)  

# Calls main function
if __name__ == '__main__':
    main()
