# importing module for generating random numbers
import random
# constant values
N_NUMBERS : int = 10  # for print only 10 numbers
MIN_VALUE : int = 1  # numbers start from 1
MAX_VALUE : int = 100  # numbers end at 100

def main():
# We use `_` instead of `i` because we don't need the value of the loop index, and using `_` makes it clear that the variable is intentionally ignored
    for _ in range(N_NUMBERS):
# calling numbers range for print
        print(random.randint(MIN_VALUE, MAX_VALUE))


if __name__ == '__main__':
    main()