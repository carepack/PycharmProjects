# 13.11.2019
# guess random number with while loop

import random
count = 0
num = random.randint(1, 9)
inp_user = 0

while inp_user != "Exit" and inp_user != num:
    count = count + 1
    inp_user = int(input("Please enter value or exit: "))
    if inp_user < num:
        print("\nSorry dude, your number is lower than we were searching for: %s" % num)
    elif inp_user > num:
        print("\nSorry dude, your number is greater than we were searching for: %s" % num)
    else:
        print("\nCongrats! Your number %s is common with the wanted %s" % (inp_user, num))
        print("Congrats! Your number {0} is common with the wanted {1} ".format(inp_user, num))
        print("\nYou've tried {0} times finding the right number".format(count))


