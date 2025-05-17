import random

words = ["apple", "banana", "grapes", "orange", "mangoes", "strawberry", "watermelon"]

def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("===Welcome to Hangman Game!===")
    print("Try to guess the word!")

    while attempts:
        print("\n Magic Word: " + display_word(word, guessed_letters))
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed the letter! Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! The letter '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("\nGame over! The word was:", word)

hangman()