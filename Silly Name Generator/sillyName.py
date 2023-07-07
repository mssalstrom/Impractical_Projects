import sys
import random



def main():
    """Choose names at random from 2 tubples of names and print to screen."""
    print("Welcome to the sidekick name picker!\n")

    first = ('Baby Oil', 'Bad News', 'Big Ups', 'Stinkbug', 'Bobby Boogerson', 'Melon Hat'
             , 'Slim Jim', 'Tire Tread', 'Meat Hook', 'Jay Low', 'Hydra', 'Shrimping Stump',
             'Nuclear', 'Paris', 'Tea Pot', 'Screen Time', 'Keyboard', 'Hacker', 'Face Melter',
             'Trippy', 'Martian Tree')

    last = ('Hootkins', 'Scrumpet', 'Minnow', 'Oxtail', 'Ribby', 'Red', 'Smallfish', 'Kingdog',
            'Tomato', 'Flaskers', 'Havvisham', 'Mushroom', 'Gnarlytown', 'Grind', 'Snuggleshine',
            'Moop', 'Belvedaire', 'Longjohn', 'Murderface', 'Pinkytoe', 'Jefferson', 'Johnson',
            'Smith', 'Quakenbush')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        # Hopefully get red output text
        print("{} {}".format(first_name, last_name), file=sys.stderr)

        try_again = input("\n\nTry again? (Press Enter or press n to quit)\n")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit")


if __name__ == "__main__":
    main()