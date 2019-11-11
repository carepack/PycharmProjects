inp_num = int(input("Bitte füttern mit einer Zahl: "))

if inp_num % 2 == 0:
    print("Es handelt sich um eine gerade Zahl\n")
else: print("Es handelt sich um eine ungerade Zahl\n")

if inp_num % 4 == 0:
    print("Es handelt sich um EIN vielfaches von 4\n")
else: print("Die Zahl ist KEIN vielfaches von 4\n")

in_num1=int(input("Bitte geben sie die erste Zahl ein: "))
in_num2=int(input("Bitte geben sie die zweite Zahl ein: "))

if in_num1 % in_num2 == 0:
    print("\nZahl 1 ist durch Zahl 2 ohne Rest teilbar")
else: print("\nZahl 1 ist durch Zahl 2 nicht ohne Rest teilbar")