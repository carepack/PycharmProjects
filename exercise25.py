# 09.12.2019
# guess game

import sys

def main():
	print("Hi, take a number from 1 to 99 and I'm goin' find them")
	run = True
	pattern = list(range(1, 101))
	min_index = 0
	max_index = len(pattern)
	mid_index = round(len(pattern) / 2)
	count = 0

	while run:
		count += 1
		high_low = input("Is your number higher or lower than: " + str(mid_index) + " if the value is correct, type correct ")
		#if high_low == "correct":
		if (mid_index - 1) == min_index or (mid_index + 1) == max_index or high_low == "correct":
		#if not mid_index != 0 or mid_index != 100:
			if high_low == "correct":
				print("The value is " + str(mid_index) + " and tried it " + str(count) + " times")
				run = False
			elif mid_index == 50:
				print("The value is " + str(mid_index) + " and tried it " + str(count) + " times")
				run = False
			elif mid_index > 50 and mid_index % 2 != 0:
				print("The value is " + str(mid_index + 1) + " and tried it " + str(count) + " times")
				run = False
			elif mid_index > 50 and mid_index % 2 == 0:
				print("The value is " + str(mid_index - 1) + " and tried it " + str(count) + " times")
				run = False
			elif mid_index < 50 and mid_index % 2 != 0:
				print("The value is " + str(mid_index + 1) + " and tried it " + str(count) + " times")
				run = False
			elif mid_index < 50 and mid_index % 2 == 0:
				print("The value is " + str(mid_index - 1) + " and tried it " + str(count) + " times")
				run = False
		elif high_low == "lower":
			max_index = mid_index
			mid_index = round((min_index + max_index) / 2)
		elif high_low == "higher":
			min_index = mid_index
			mid_index = round((min_index + max_index) / 2)
		else:
			print(" Value is 100 or 0")


if __name__ == '__main__':
	if sys.version_info[0] < 3:
		raise Exception("Minimum requirement: Python3")
	main()