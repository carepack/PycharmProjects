# 15.11.2019
# deduplicate with sets. refactor exercise 5 with sets

import random

# begin function -----------------------------
def list_gen():
    get_out = ""
    new_list = []
    while get_out != "exit":
        get_out = input("Please enter number or string, but always the same type. Type exit to go out: ")
        if get_out != "exit":
            new_list.append(get_out)
    return new_list

def rem_dup(user_list):
    user_list = set(user_list)
    return user_list



# exercise 5 solution with set
def ex5_ran_lists():
    c = []
    ran_num1 = random.randint(5,10)
    ran_num2 = random.randint(5,10)

    # random.sample generates no duplicates
    a = random.sample(range(15), ran_num1)
    b = random.sample(range(15), ran_num2)

    print(a)
    print(b)

    c = set(a) - set(b)
    return c
# end function -----------------------------

def list_gen():
choice = input("What do you want to deduplicate? Enter random for auto lists or manual to input values: ")
if choice == "random":
    print(str(ex5_ran_lists()))
else:
    user_list = list_gen()
    print(user_list)
    print(str(rem_dup(user_list)))




