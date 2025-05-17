# -------------------PROBLEM STATEMENT:
'''
Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
-Assume for now that the minimum height is 50.
'''

# constant height limit
minimum_height = 50

def main():
# input height from user
    input_height = float(input("Enter your Height: "))
# checks if height is >= to height limit then statement will be true otherwise if will false
    if input_height >= minimum_height:
        print("You can go for a ride!")
    else:
        print("Sorry! You're not tall enough for ride.")

# calling function
if __name__ == "__main__":
    main()