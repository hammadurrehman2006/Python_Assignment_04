# ---------------------PROBLEM STATEMENT:
'''
Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!). 
'''

# maximum value up to which Fibonacci numbers will be printed
MAX_VALUE = 10000

def main():
    current = 0  # The 0th Fibonacci Number
    next_num = 1  # The 1st Fibonacci Number
# Loop to print Fibonacci numbers as long as the current number is <= MAX_VALUE
    while current <= MAX_VALUE:
        print(current)
# Calculate the next Fibonacci number
        next_num = current + next_num
# Move to the next term in the sequence
        current = next_num
# Update next_num to the new Fibonacci number
        next_num = next_num

# calling main function
if __name__ == "__main__":
    main()