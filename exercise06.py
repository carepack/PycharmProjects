# 13.11.2019
# check input_string if reads same forwards and backwards
# a = [5, 10, 20, 25, 34]
# a[3]
# =25

in_string = input("Please enter word: ")
len_string = int(len(in_string)-1)
rev_string = in_string[::-1] #-1 every character backwards

if in_string == rev_string:
        print("\nCommon for and backwards..... " + in_string + " " + rev_string)

