# 13.12.2019
# get user input an manipulate strings

from datetime import date

name=input("Whats your name: ")
age=input("How old are you: ")
print("Your name: " +name)
print(name + ", you are " + age + " old")

curr_year = date.today().year
est_year = 100 - int(age) + curr_year
est_year = str(est_year)
line_out="In the year: " + est_year + " you'll be 100 years!\n"
print(line_out)
line_count=input("How often repeat the input? ")
line_count=int(line_count)

for i in range(line_count):
    print(line_out)


print(line_out * 5)