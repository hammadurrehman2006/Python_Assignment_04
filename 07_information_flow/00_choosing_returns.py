# ---------------------PROBLEM STATEMENT:
'''
There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!
'''

# Defining the legal adult age
LEGAL_ADULT_AGE = 18

# Function to check if the person is an adult
def check_if_adult(age: int):
    if age >= LEGAL_ADULT_AGE:
# Returns True if the age is greater than or equal to 18
        return True
 # Returns False if the age is less than 18  
    return False

def main():
    user_age = int(input("Please enter the person's age: "))  # Input for age
    is_adult = check_if_adult(user_age)  # Check if the person is an adult
    print(is_adult)  # Print the result (True or False)

# calling main function
if __name__ == "__main__":
    main()
