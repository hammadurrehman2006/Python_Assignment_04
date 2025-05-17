# ------------------------PROBLEM STATEMENT:
'''
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
'''

# function for user input
def user_numbers():
# empty list to store the numbers
    user_num = []

    while True:
# input field
        user_input = input("Enter the number: ")
# break the loop
        if user_input == "":
            break
# convert user input into integer and append in list
        num = int(user_input)
        user_num.append(num)
# returns the list
    return user_num

# cpunting numbers in dictionary
def count_numbers(num_lst):
# empty dictionary
    number_dict = {}

    for num in num_lst:
# if the number is not in dict then add it with the count of 1
        if num not in number_dict:
            number_dict[num] = 1
# if the number is in the dict then do an increment in the number
        else:
            number_dict[num] += 1
# return dict numbers 
    return number_dict

# function for printing
def count_print(number_dict):
# loop through dict and print on count
    for num in number_dict:
        print(str(num) + " appears " + str(number_dict[num]) + " times.")

def main():
# call the function to get the number from user
    user_num = user_numbers()
# call the function to count the frequency of each number
    number_dict = count_numbers(user_num)
# call the function to print the counts
    count_print(number_dict) 

# calling main function
if __name__ == "__main__":
    main()