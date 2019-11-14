# 13.11.2019
# Auf Primzahl prüfen mit verwenden einer Funktion
# while / else wird ausgeführt wenn while Bedingung false bekommt / Zähler abgelaufen ist

def find_prime(user_value):
    i = 2
    while i < (user_value):
        prime = user_value % i
        if prime != 0:
            i += 1
        else:
            return ("ist keine Primzahl da durch %s teilbar" % i)
    else:
        return ("%s ist eine Primzahl" % user_value)


user_in = int(input("Bite eine Zahl eingeben: "))

if user_in == 1:
    print("1 zählt nicht")
else:
    print("Ihre Zahl " + str(find_prime(user_in)))