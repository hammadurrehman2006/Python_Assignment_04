# ---------------------PROBLEM STATEMENT:
'''
There are times where we want to return different things from a function based on some condition. To practiImplement the following function which takes in 3 integers as parameters:
def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """
'''

def in_range(n, low, high):
# Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low.
    if low <= n <= high:
        return True
    return False

def main():
# Test cases
    print(in_range(5, 1, 10))  # Should print: True
    print(in_range(0, 1, 10))  # Should print: False
    print(in_range(15, 1, 10)) # Should print: False
    print(in_range(7, 5, 10))  # Should print: True

# call the main function
if __name__ == '__main__':
    main()
