# ---------------------PROBLEM STATEMENT:
'''
Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.
'''

def main():
# Initialize with input method......without input we'll go like this num: int = 7
    num = int(input("Enter an integer number: "))
# Call the subtract_seven function
    num = subtract_seven(num)
# Print the result
    print("This should be zero:", num)

def subtract_seven(num):
# Subtract 7 from the input number
    num = num - 7
    return num

# Calls main function
if __name__ == '__main__':
    main()
