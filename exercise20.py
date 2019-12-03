# 03.12.2019
# Binary search in a list if the guess is in

import sys



def main():
    run = True
    ordered_List = [9, 16, 33, 67, 118, 119, 143, 149, 160]
    guess = int(input("Please give number"))
    len_list = round(len(ordered_List) / 2)
    print(str(ordered_List[len_list]))
    #print(len_list)
    while True:

        if len_list == 0 or len_list >= (len(ordered_List) - 1):
            print("Number not included in list")
            return False

        if guess == ordered_List[len_list]:
            print ("Thats your Number: " + str(ordered_List[len_list]))
            return False
        elif guess < ordered_List[len_list]:
            len_list -= 1
        elif guess > ordered_List[len_list]:
            len_list += 1



    #else:
    #    print("Number not included in list!")






if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    main()