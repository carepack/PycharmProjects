# 14.11.2019
# print out first / last value of a list with functions and user input

a = []
b = []
user_in = ""

def get_fifo(a_list):
    b.append(a[0])
    b.append(a[-1])
    return b

def get_input(user_val):
    while user_val != "exit":
        user_val = input("Input number or exit: ")
        if user_val != "exit":
            a.append(user_val)

get_input(user_in)
print(get_fifo(a))
