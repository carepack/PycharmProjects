# 13.11.2019
# check for prime numbers with function
# while / else is executed if while condition becomes true / counter expires

def find_prime(user_value):
    i = 2
    while i < (user_value):
        prime = user_value % i
        if prime != 0:
            i += 1
        else:
            return ("is not a prime number because dividable by %s" % i)
    else:
        return ("%s is a prime number" % user_value)


user_in = int(input("Please enter number: "))

if user_in == 1:
    print("1 doesn't count")
else:
    print("Your number " + str(find_prime(user_in)))