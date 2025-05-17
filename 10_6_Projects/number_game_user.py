import random

lower = 0
higher = 15

print("Hi! Think about any number, and I'll try to guess it right! 🎯")

while True:
  guessed_number = random.randint(lower, higher)
  print(f"Is {guessed_number} your guessed number? ")

  message = input("Enter 'r' if the guess is right ✅, 'h' if the guess is high ⬆️, 'l' if the guess is low ⬇️: ").lower()

  if message == "r":
        print(f"Yay! 🎉 I guessed your number: {guessed_number}")
        break
  elif message == "h":
        higher = guessed_number - 1
        print("Okay, I'll guess lower next time! ⬇️")
  elif message == "l":
        lower = guessed_number + 1
        print("Got it! I'll guess higher next time! ⬆️")
  else:
        print("Oops! 🚫 Invalid input! Please enter 'r', 'h', or 'l'.")