# 15.11.2019
# generate fibonacci numbers with function

def gen_fibo(user_val):
    i = 0
    j = 1
    count = 0
    a = [0, 1]
    while count < (user_val - 2):
        a.append(a[i] + a[j])
        i += 1
        j += 1
        count += 1
    return a

user_in = int(input("Please enter how many fibonacci  numbers you want: "))
print(str(gen_fibo(user_in)))