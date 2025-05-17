# -------------------PROBLEM STATEMENT:
'''
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd
'''

# Checks if a number is odd. Returns True if it is odd, otherwise False.
def is_odd(value: int):
# Return True if the number is odd (remainder 1 when divided by 2)
    return value % 2 != 0  

def main():
# Loop through numbers from 10 to 19
    for number in range(10, 20): 
 # Check if the number is odd
        if is_odd(number): 
            print(number, 'odd')  # If it's odd, print 'odd'
        else:
            print(number, 'even')  # If it's even, print 'even'

# call the main function
if __name__ == '__main__':
    main()
