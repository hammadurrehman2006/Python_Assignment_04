# -------------------PROBLEM STATEMENT:
'''
Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
'''

def main():
# Ask the user for a number and also convert it into integer
    curr_value = int(input("Enter a number: "))
# Repeat doubling the number until it is 100 or greater
    while curr_value < 100:
# Double the current value
        curr_value = curr_value * 2
# Print the doubled value on the same line
        print(curr_value, end = " ")
# Print a newline after the loop ends
    print()
    
# Calling main function
if __name__ == "__main__":
    main()