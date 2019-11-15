# 15.11.2019
# juggle with strings and lists - sentence reverse order

def rev_order(user_in):
    w_count = len(user_in)
    list = []
    for element in user_in:
        list.append(user_in[w_count-1])
        w_count -= 1
    return list

user_in = input("give me a sentence: ").split()
print(str(rev_order(user_in)))
