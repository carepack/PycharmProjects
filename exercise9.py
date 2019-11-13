import random
count = 0
num = random.randint(1, 9)
inp_user = 0

while inp_user != "Exit" and inp_user != num:
    count = count + 1
    inp_user = int(input("Bitte eine Zahl oder Exit eingeben: "))
    if inp_user < num:
        print("\nLeider nein, ihre Zahl liegt unterhalb der gesuchten: %s" % num)
    elif inp_user > num:
        print("\nLeider nein, ihre Zahl liegt oberhalb der gesuchten: %s" % num)
    else:
        print("\nHerzlichen Glückwunsch! ihre Zahl %s stimmt mit der gesuchten Zahl %s überein" % (inp_user, num))
        print("Herzlichen Glückwunsch! ihre Zahl {0} stimmt mit der gesuchten Zahl {1} überein".format(inp_user, num))
        print("Sie haben {0} Versuche gebraucht, um die richtige Zahl zu finden".format(count))


