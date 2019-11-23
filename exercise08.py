# 13.11.2019
# gameplay stone, siccors, paper
# call via function

def comp_answer(answ_1, answ_2):
    if answ_1 == answ_2:
        print("\nNobody wins - both selected %s !" % choice_p1)
    elif answ_1 == "Stone":
        if answ_2 == "Paper":
            return("Paper wins")
        else:
            return("Stone wins")
    elif answ_1 == "Paper":
        if answ_2 == "Scissors":
            return("Scissors wins")
        else:
            return("Paper wins")
    elif answ_1 == ("Scissors"):
        if answ_2 == ("Stone"):
            return("Stone wins")
        else:
            return("Scissors wins")
    else:
        return("Can't compute input")
        sys.exit()



str = "yes"

while str == "yes":
    player_1 = input("Name player 1: ")
    player_2 = input("Name player 2: ")
    choice_p1 = input("%s, choose you stone, scissors or paper? " % player_1)
    choice_p2 = input("%s, choose you stone, scissors or paper? " % player_2)
    print(comp_answer(choice_p1, choice_p2))
    str = input("Play again yes or no: ")
