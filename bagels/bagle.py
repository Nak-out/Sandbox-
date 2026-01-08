import random

n = 3
max_try = 10

def getSecretNum(n):
    secret_number = ""
    mylist = list("0123456789")
    random.shuffle(mylist)
    for i in mylist[:n]:
        secret_number += i
    return secret_number
    
def getClues(guess, secret_num):
    if guess == secret_num:
        return "You GOT IT!!"
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("FERMI")
        elif guess[i] in secret_num: 
            clues.append("PICO")
    
    if len(clues) == 0:
        return "\nBAGLE"
    else: 
        clues.sort()
        return " ".join(clues)

def main():
    print("\n" + "=" * 90)
    print("""
    Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    """)
    print("=" * 90)
    print(f"""
    I am thinking of a {n}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
          
    When I say: That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.

    Ready?
    """)

    while True:

        secret_num = getSecretNum(n=n)

        guess_try = 0

        while guess_try < max_try:

            guess = ""

            while len(guess) != n or not guess.isdecimal():
                print(f"\nGuess #{guess_try +1}:")
                guess = input(">")
                
            guess_try += 1
            print(getClues(guess=guess, secret_num=secret_num))
            if guess == secret_num:
                break
        
        if guess_try == max_try:
            print(f"""
            nice try!!
            The correct answer was {secret_num}.          
            """)

        print(f"\nWanna try again? Y/N")
        inp = input(">")
        if inp.lower() == "n":
            break

if __name__ == "__main__":
    main()

                

