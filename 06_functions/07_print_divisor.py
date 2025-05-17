# -------------------PROBLEM STATEMENT:
'''
Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!
'''

# Function to print all divisors of a given number
def show_divisors(number: int):
    print("Here are the divisors of", number)
# Loop through numbers from 1 to number (inclusive)
    for divisor in range(1, number + 1): 
# Check if 'divisor' is a divisor of 'number' 
        if number % divisor == 0:  
            print(divisor)

def main():
 # Ask user for a number
    number = int(input("Enter a number: ")) 
# Call the show_divisors function
    show_divisors(number)  

# calling main function
if __name__ == '__main__':
    main()
