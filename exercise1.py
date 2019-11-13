# 13.12.2019
# Eingaben einlesen und Strings manipulieren

from datetime import date

name=input("Wie ist dein Name: ")
age=input("Wie alt bist du: ")
print("du heißt: " +name)
print(name + ", du bist " + age + " alt")

curr_year = date.today().year
est_year = 100 - int(age) + curr_year
est_year = str(est_year)
line_out="Im Jahr: " + est_year + " wirst du 100 Jahre alt sein!\n"
print(line_out)
line_count=input("Wie oft soll die Ausgabe wiederholt werden? ")
line_count=int(line_count)

for i in range(line_count):
    print(line_out)


print(line_out * 5)