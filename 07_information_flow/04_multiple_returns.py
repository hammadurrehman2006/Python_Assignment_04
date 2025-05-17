# ---------------------PROBLEM STATEMENT:
'''
There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.
'''

def gather_user_data():
# Asking for user data with different phrasing
    first_name_input = input("Please enter your first name: ")
    last_name_input = input("Please enter your last name: ")
    email_input = input("Please enter your email address: ")
    
# Returning the values as a tuple in a different way
    user_details = (first_name_input, last_name_input, email_input)
    return user_details

def main():
# Call the gather_user_data function to collect the data
    data = gather_user_data()
    
# Printing the received data in a more descriptive format
    print("The data you provided is:", data)

if __name__ == "__main__":
    main()
