# -------------------PROBLEM STATEMENT:
'''
Write a function that takes two numbers and finds the average between the two.
'''

def calculate_average(x: float, y: float):
# Sum the two numbers
    total = x + y 
# Return the average by dividing the total by 2
    return total / 2

def main():
# Calculate the average of two different pairs of numbers
    first_avg = calculate_average(0, 15)  # Average of 0 and 10
    second_avg = calculate_average(10, 15)  # Average of 8 and 10
    
# Calculate the average of the two previously calculated averages
    overall_avg = calculate_average(first_avg, second_avg)
    
# Print the results
    print("first_avg:", first_avg)  # Output: 5.0
    print("second_avg:", second_avg)  # Output: 9.0
    print("overall_avg:", overall_avg)  # Output: 7.0
    
#  calling main function.
if __name__ == '__main__':
    main()
