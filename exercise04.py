# 13.11.2019
# identify divisors of number. ouput as list

in_num = int(input("Please enter number: "))

x_ra = range(2, in_num+1)
for element in x_ra:
    res = in_num % element
    if res == 0:
        out_num = str(in_num)
        out_element = str(element)
        out_divisor = str(in_num / element)
        print("Your number " + out_num + " is dividable by " + out_element + " result = " + out_divisor)

# output as list
num_div = []
for element in x_ra:
    if in_num % element == 0:
        num_div.append(element)
print("Divisors as list: " + str(num_div))