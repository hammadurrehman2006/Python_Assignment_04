def main():
# Get user input
    curr_value = int(input("Enter a number: "))
    
# Continue doubling the number until it is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value)  # Print the doubled value

if __name__ == '__main__':
    main()
