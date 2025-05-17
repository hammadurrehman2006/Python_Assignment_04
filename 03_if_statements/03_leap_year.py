# -------------------PROBLEM STATEMENT:
'''
Write a program that reads a year from the user and tells whether a given year is a leap year or not.
-The given year must be evenly divisible by 4;
-If the year can also be evenly divided by 100, it is NOT a leap year; unless:
-The year is also evenly divisible by 400. Then it is a leap year.
'''

def main():
# user inputs the year
    year = int(input("Enter the year: "))

    if year % 4 == 0: # checks if the year is evenly divisible by 4
        if year % 100 == 0: # checks if the year is evenly divisible by 100
            if year % 400 == 0: # checks if the year is evenly divisible by 400
                print("It's a leap year!")
            else:
                print("It's not a leap year!")
        else:
            print("It's a leap year!")
    else:
        print("It's not a leap year!")
# calling function
if __name__=="__main__":
    main()