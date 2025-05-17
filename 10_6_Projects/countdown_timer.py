import time

def countdown(seconds):
    while seconds >= 0:
        mins = seconds // 60
        sec = seconds % 60

        timer = f"{mins:02}:{sec:02}"
        print(timer, end="\r")

        time.sleep(1)
        seconds -= 1

    print("Time's up! 00:00")

input_seconds = int(input("Enter the time in seconds: "))

countdown(input_seconds)
