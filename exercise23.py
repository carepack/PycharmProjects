# 06.12.2019
# File overlap

import sys

def main():
    happy_list = []
    prime_list = []
    with open('happynumbers.txt', 'r') as happy_source:
        with open('primenumbers.txt', 'r') as prime_source:
            for line in happy_source:
                happy_list.append(happy_source.readline().replace("\n",""))
                #happy_list.append(int(happy_source.readline()))
            for line in prime_source:
                prime_list.append(prime_source.readline().replace("\n", ""))
                #prime_list.append(int(prime_source.readline()))
            common_numbers = [el for el in happy_list if el in prime_list]
    print(common_numbers)

if __name__ == '__main__':
    if sys.version_info[0] <3 :
        raise Exception("Minimum requirement: Python3")
    main()
