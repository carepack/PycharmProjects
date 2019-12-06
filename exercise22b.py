# 05.12.2019
# Read from file an work with the strings

import sys

def main():
    counter_dict = {}
    with open("Training_01.txt", "r") as source_file:
        line = source_file.readline()
        while line:
            line = line[3:-26]
            if line in counter_dict:
                counter_dict[line] +=1
            else:
                counter_dict[line] = 1
            line = source_file.readline()
    print(counter_dict)

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("At least python3 required")
    main()
