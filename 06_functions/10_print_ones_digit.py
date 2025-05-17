# -------------------PROBLEM STATEMENT:
'''
Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!
'''

# Function to print the ones digit of a number
def print_ones_digit(num):
# Using % to get the ones digit
    print("The ones digit is", num % 10)  


def main():
# Get number input from the user
    num = int(input("Enter a number: "))  
# Call the function to print the ones digit
    print_ones_digit(num)  

# Call the main function
if __name__ == '__main__':
    main()  
