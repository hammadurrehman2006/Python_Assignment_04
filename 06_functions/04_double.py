# -------------------PROBLEM STATEMENT:
'''
Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
'''

# Function to return double the given number
def multiply_by_two(value: int):
    # Multiply the number by 2 and return the result
    return value * 2 

def main():
# Ask user to enter a number
    user_input = int(input("Enter a number: "))
# Call the multiply_by_two function with the entered number  
    doubled_value = multiply_by_two(user_input)
# Print the result
    print("Double that is", doubled_value) 

# Call the main function
if __name__ == '__main__':
    main() 
