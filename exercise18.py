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

def run_game(random_digit):
    guess = ''
    while guess != random_digit:
        guess = input("Please enter your Number: ")

def main():
    random_digit = gen_digit()
    run_game(random_digit)

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    main()
