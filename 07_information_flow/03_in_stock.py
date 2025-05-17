# ---------------------PROBLEM STATEMENT:
'''
Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory.
'''

def main():
# Step 1: Prompt user for a fruit
    fruit = input("Enter a fruit: ")
# Step 2: Get the number of fruits in stock using num_in_stock
    stock = num_in_stock(fruit)
# Step 3: Print the appropriate message based on the stock count
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# This function returns the number of the specified fruit in stock
def num_in_stock(fruit):
# Predefined fruits and their stock counts
    if fruit == 'apple':
        return 22
    if fruit == 'durian':
        return 40
    if fruit == 'pear':
        return 100
    if fruit == 'mangos':
        return 143
    if fruit == 'peach':
        return 80
    if fruit == 'oranges':
        return 76
    else:
# If the fruit is not listed, return 0
        return 0

# calls the main function
if __name__ == '__main__':
    main()
