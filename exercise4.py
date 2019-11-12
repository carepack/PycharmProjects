in_num = int(input("Bitte eine Zahl eingeben: "))

x_ra = range(2, in_num+1)
for element in x_ra:
    res = in_num % element
    if res == 0:
        out_num = str(in_num)
        out_element = str(element)
        out_divisor = str(in_num / element)
        print("Ihre Zahl " + out_num + " ist durch " + out_element + " teilbar = " + out_divisor)

# output as list
num_div = []
for element in x_ra:
    if in_num % element == 0:
        num_div.append(element)
print("Teiler als Liste: " + str(num_div))