# -------------------PROBLEM STATEMENT:
'''
Fill out the function count_even(lst) which first populates a list by prompting the user for integers 
until they press enter (please use the prompt "Enter an integer or press enter to stop: "),
and then prints the number of even numbers in the list.
'''

# Function to count even numbers in a list
def count_even(lst):
# initial number of count is 0
    count = 0
    for number in lst:
# check if the number is even
        if number % 2 == 0:
# increment in number if the count is even
            count += 1
    print(count)

# function to get integer from user
def list_ints():
# empty list
    lst = []
    user_input = input("Enter an integer or press enter to stop the process: ")
# runs if user press enter without giving any number
    while user_input != "":
# convert in integer and add in list
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop the process: ")
# returns the list of integer
    return lst

def main():
# get list of integer from user
    lst = list_ints()
# count and print even numbers in list
    count_even(lst)

# calling function
if __name__ == "__main__":
    main()