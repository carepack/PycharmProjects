# 05122019
# Reading from file

import sys

def main():
    nf_list = []
    with open('nameslist.txt', "r") as n_list:
        for line in n_list:
            nf_list.append(line.replace("\n", ""))
        i = 0
        darth_count = 0
        lea_count = 0
        luke_count = 0

        for elements in nf_list:
            if nf_list[i] == "Darth":
                darth_count += 1
                i += 1
            elif nf_list[i] == "Luke":
                luke_count += 1
                i += 1
            elif nf_list[i] == "Lea":
                lea_count += 1
                i += 1

        print("The name Luke has been found " + str(luke_count) + " times")
        print("The name Lea has been found " + str(lea_count) + " times")
        print("The name Darth has been found " + str(darth_count) + " times")

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python version has to be 3")
    main()