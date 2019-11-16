#!/opt/local/bin/python3.7
# 16.11.2019
# simple pw generator - main func, join, secrets ad check python version
# executable from commandline

import sys
import string
import secrets

def choice():
    user_in = input("Choose your password complexity and enter the length: ")
    return user_in

def gen_pw(answ):
    signs = str.strip(string.printable)
    password = ''.join(secrets.choice(signs) for i in range(int(answ)))
    print(password)
    once_again = input("Generate another one: yes / no? ")
    if once_again == "yes":
        main()
    else:
        return

def main():
    answ = choice()
    gen_pw(answ)

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    main()
