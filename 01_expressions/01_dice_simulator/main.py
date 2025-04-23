import random

NUM_SIDES = 6

def roll_dice():
  
    dice1: int = random.randint(1, NUM_SIDES)
    dice2: int = random.randint(1, NUM_SIDES)
    total: int = dice1 + dice2
    print("Total of two dice:", total)

def main():
    dice1: int = 10
    print("dice1 in main() starts as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("dice1 in main() is: " + str(dice1))


if __name__ == '__main__':
    main()