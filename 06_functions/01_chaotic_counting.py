# -------------------PROBLEM STATEMENT:
'''
Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. 
We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, 
you should call done() and check if it returns True or not. If done() returns True, 
we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), 
which will print "I'm done.". We've written main() for you -- check it out! 
Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.
'''

import random

# Set the likelihood that 'done' will return True to 10%
DONE_LIKELIHOOD = 0.1  # 10% chance to stop

def chaotic_counting():
    # Count from 1 to 10
    for i in range(10):
        curr_num = i + 1  # Current number to print
        if done():
            # Stop the counting early and return control back to main
            return
        print(curr_num)  # Print the current number

def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    # Start the counting
    chaotic_counting()  
    # This will print once chaotic_counting finishes
    print("I'm done")  

# Calls main function to start the program
if __name__ == "__main__":
    main()

