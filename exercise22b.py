# 05.12.2019
# Read from file an work with the strings
# /a/anechoic_chamber/sun_agrlvogbxdobprem.jpg
import sys
from array import *





def main():
    file_list = []
    column = []
    tmp  =[]
    dict = {}
    with open("Training_01.txt", "r") as source_file:
        for lines in source_file:
            file_list.append(lines.replace("\n", ""))
            tmp = lines.split("/", 3)
            dict['1'] = tmp[1]
            dict['2'] = tmp[2]
            print(dict)
            #column[0].append(tmp[1])
            #column[0][0].append(tmp[2])
            #column[0][0][0].append(tmp[3])
        print(tmp)


        #for el in file_list:
            #el.strip()
        #    print(el)






if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("At least python3 required")
    main()
