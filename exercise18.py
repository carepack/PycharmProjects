# 23.11.2019
# Cows and Bulls Game

import string
import sys
from random import choice


def gen_digit():
    numbers = string.digits
    sec_digit = ''.join(choice(numbers) for element in range(4))
    print(sec_digit)
    return sec_digit

def run_game(random_digit, guess):
    i = 0
    cowbull = [0,0]
    guess = list(guess)
    random_digit = list(random_digit)
    for i in range(len(random_digit)):
        if random_digit[i] == guess[i]:
            cowbull[1] +=1
            i += 1
        elif guess[i] in random_digit: # and not cowbull:
            print(str(guess))
            cowbull[0] +=1
            i += 1
    return cowbull

def main():
    playgame = True
    tries = 0
    random_digit = gen_digit()
    while playgame:
        guess = input("Please enter your guess: ")
        if guess == exit:
            break
        bullcow_count = run_game(random_digit, guess)
        tries += 1

        print("You have " + str(bullcow_count[1]) + " bulls and " + str(bullcow_count[0]) + " cows")

        if bullcow_count[1] == 4:
            playgame = False
            print("You tried it " + str(tries) + " times and the right number is: " + str(random_digit))
        else:
            print("No luck, go on and try again")

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    main()
