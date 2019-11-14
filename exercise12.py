# 14.11.2019
# Print out first / last value of a list with functions and user input

a = []
b = []
user_in = ""

def get_fifo(a_list):
    b.append(a[0])
    b.append(a[-1])
    return b

def get_input(user_val):
    while user_val != "Exit":
        user_val = input("Zahl eingeben oder Exit: ")
        if user_val != "Exit":
            a.append(user_val)

get_input(user_in)
print(get_fifo(a))
