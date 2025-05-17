# -------------------PROBLEM STATEMENT:
'''
Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
'''

# importing time module for printing after second
import time 

def main():
# Start from 10, stop at 1, step by -1
    for i in range(10, 0, -1):
        print(i)
# Wait for 1 second before printing the next number
        time.sleep(1)
# Print Liftoff after the countdown
    print("=========Liftoff!=========")
    
# Call the main function
if __name__ == "__main__":
    main()