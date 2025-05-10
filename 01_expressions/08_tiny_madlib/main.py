starting_sentence: str = "The adventurous scientist decided to " # verb the adjective noun.

def main():
    adjective: str = input("Please enter an adjective.  ")
    noun: str = input("Please enter a noun.  ")
    verb: str = input("Please enter a verb.  ")
    print(starting_sentence + verb + " the " + adjective + " " + noun + ".")


if __name__ == '__main__':
    main()