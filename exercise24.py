# 06.12.2019
# game board fake graphics printing with functions

import sys

def draw_dot(x):
    d = 0
    while d < x:
        if d < (x - 1):
            print(" ...", end = "")
            d += 1
        else:
            print(" ...")
            d += 1

def draw_lines(x):
    d = 0
    while d < x:
        if d < (x - 1):
            print("|   ", end = "")
            d += 1
        else:
            print("|   ")
            d += 1

def main():
    board_size = int(input("Please enter the gameboard size: "))
    x = board_size
    y = board_size + 1
    i = 0

    #while i < y:
    for index in range(y):
        if i < x:
            draw_dot(x)
            draw_lines(y)
            i += 1
        else:
            draw_dot(x)
            i += 1

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Minimum requirement: Python3")
    main()