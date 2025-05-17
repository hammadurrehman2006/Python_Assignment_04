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

if __name__ == "__main__":
    main()