# -------------------PROBLEM STATEMENT:
'''
Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
'''

def main():
# using for loop to initialize the even numbers starts from 0 to 19 but its actually 20 numbers in counting
    for i in range(20):
# in this line i'm using {i + 1} this for print total numbers in counting and {i * 2} for multiplying the numbers with 2 for even numbers 
        print(f"Number {i + 1}... {i * 2}")
# calling the main function
if __name__ == "__main__":
    main()

