import random

while str != "Exit":
    num = random.randint(1,9)
    print(num)
    inp_user = int(input("Bitte eine Zahl eingeben: "))
    if inp_user < num:
        print("\nLeider nein, ihre Zahl liegt unterhalb der gesuchten: %s" % num)
    elif inp_user > num:
        print("\nLeider nein, ihre Zahl liegt oberhalb der gesuchten: %s" % num)
    else:
        print("\nHerzlichen Glückwunsch! ihre Zahl %s stimmt mit der gesuchten Zahl %s überein" % (inp_user, num))
        print("Herzlichen Glückwunsch! ihre Zahl {0} stimmt mit der gesuchten Zahl {1} überein".format(inp_user, num))
    str = input("\nZum beenden bitte Exit eingeben:\n ")


