# ------------------------PROBLEM STATEMENT:
'''
Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
'''

def main():
# dictionary of fruits
    fruits = {'apple': 100, 'mango': 50, 'dragonfruit': 200, 'strawberry': 10, 'grapes': 1.5, 'orange': 5}
# initial cost = 0 
    cost = 0
# for loop for fruit in fruits
    for fruit in fruits:
        price = fruits[fruit]
        message = int(input("How many (" + fruit + ") do you want to buy?: "))
        cost += (price * message)
    print("Your total is $" + str(cost))

# calling function
if __name__ == '__main__':
    main()