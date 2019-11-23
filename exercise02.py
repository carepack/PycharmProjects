# 13.11.2019
# identify even / odd numbers. specified / input

inp_num = int(input("Please input value: "))

if inp_num % 2 == 0:
    print("It's an even number\n")
else: print("It's an odd number\n")

if inp_num % 4 == 0:
    print("It's a multiple of 4\n")
else: print("It's not a multiple of 4\n")

in_num1=int(input("Please enter the first number: "))
in_num2=int(input("Please enter the second number: "))

if in_num1 % in_num2 == 0:
    print("\nNumber 1 is dividable by 2 without rest")
else: print("\nNumber 1 is not dividable by 2 without rest")