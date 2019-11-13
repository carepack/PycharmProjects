# 13.11.2019
# Prüfe input_string ob von hinten und vorne gleich gelesen. Zugirff auf List Index
# a = [5, 10, 20, 25, 34]
# a[3]
# =25

in_string = input("Bitte, ein Wort eingeben: ")
len_string = int(len(in_string)-1)
rev_string = in_string[::-1] #-1 every character backwards

if in_string == rev_string:
        print("\nVon hinten wie von vorne..... " + in_string + " " + rev_string)

