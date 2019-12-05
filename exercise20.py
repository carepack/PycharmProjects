# 03.12.2019
# Binary search in a list if the guess is in

import sys

def bin_search(ordered_List, guess):
    start_index = 0
    end_index = len(ordered_List) - 1
    l = 0

    while l < len(ordered_List) - 1:
        middle_index = round((end_index + start_index) / 2)

        middle_element = ordered_List[middle_index]

        if middle_element == guess:
            print("Congrats, the number is in the list: " + str(ordered_List[middle_index]))
            return True
        elif guess < middle_element:
            end_index = middle_index
            l += 1
        elif guess > middle_element:
            start_index = middle_index
            l += 1
    else:
        print("Out of range: number not in list")
        return False

def main():
    ordered_List = [9, 16, 33, 67, 118, 119, 143, 149, 160]
    guess = int(input("Please enter your number: "))
    print(bin_search(ordered_List, guess))

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    main()