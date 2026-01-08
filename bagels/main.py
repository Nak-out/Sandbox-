"""Bagels, by Al Sweigart al@inventwithpython.com
 A deductive logic game where you must guess a number based on clues.
 View this code at https://nostarch.com/big-book-small-python-projects
 A version of this game is featured in the book "Invent Your Own
 Computer Games with Python" https://nostarch.com/inventwithpython
 Tags: short, game, puzzle"""

import random
import sys 

def gen():
    random.seed()
    digit_number = str(
        random.randrange(100, 999)
    )
    return digit_number

print("=" * 70)
print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com.""")
print("=" * 70 + "\n")
print(f"I'm thinking of a 3 digit number, can you guess it?")
print("""
here are some clues :
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.
 """)

result = None

while(True):
    digit_number = gen()
    trys = 10
    print("\nI have thought up a number")
    print("\nYou have 10 guesses to get it. Ready?\n")
    while(trys > 0):
        print(f"Guess #{11 - trys}\n")
        guess = input()
        if guess.lower() == "exit":
            sys.exit(1)
        if guess.isalpha(): 
            print("\nERROR! enter a 3 digit number\n")
            continue
        if len(guess) != 3:
            print(f"\nERROR!!! 3 digit number required! try again!\n")
            continue
        else: 
            if guess == digit_number:
                break
            if (guess[0] not in digit_number
                and guess[1] not in digit_number
                and guess[2] not in digit_number) :
                print("*" * 70)
                print("BAGELS!! Try again!")
                print("*" * 70)
                trys -= 1
                continue
            else:
                for i in range(3):
                        if guess[i] == digit_number[i]:
                            result = "FERMI"
                            break
                if result is None:
                    print("*" * 70)
                    print("PICO!! Try again!")
                    print("*" * 70)
                    trys -= 1
                    continue
                else:
                    print("*" * 70)
                    print("Fermi!! Try again!")
                    print("*" * 70)
                    trys -= 1
                    continue  

    if trys > 0:
        print("*" * 70)
        print("YOU WON!!!")
        print("*" * 70 + "\n")
        print("Do you want to play again? y/n/exit")
        play_again = input()
        if play_again.lower() == "y":
            continue
        elif play_again.lower() == "exit":
                sys.exit(1)
        else: break 
    else: 
        print("YOU LOST, wanna try again? y/n/exit")
        play_again = input()
        if play_again.lower() == "y":
            continue
        else: sys.exit(1)
    