def comp_answer(answ_1, answ_2):
    if answ_1 == answ_2:
        print("\nKeiner gewinnt - beiden haben %s gewählt!" % choice_p1)
    elif answ_1 == "Stein":
        if answ_2 == "Papier":
            return("Papier gewinnt")
        else:
            return("Stein gewinnt")
    elif answ_1 == "Papier":
        if answ_2 == "Schere":
            return("Schere gewinnt")
        else:
            return("Papier gewinnt")
    elif answ_1 == ("Schere"):
        if answ_2 == ("Stein"):
            return("Stein gewinnt")
        else:
            return("Schere gewinnt")
    else:
        return("Eingabe kann nicht verarbeitet werden")
        sys.exit()



str = "Ja"

while str == "Ja":
    player_1 = input("Name Spieler 1: ")
    player_2 = input("Name Spieler 2: ")
    choice_p1 = input("%s, wählst du Stein, Schere oder Papier? " % player_1)
    choice_p2 = input("%s, wählst du Stein, Schere oder Papier? " % player_2)
    print(comp_answer(choice_p1, choice_p2))
    str = input("Nochmal spielen? Ja oder Nein eingeben: ")
