# 09.12.2019
# guess game

import sys

#def search_guess(g, max, mid, c):












def main():
	guess = int(input("Welcome to the game, I'll look how often I have to check guess until I find your number. Input (0 - 100): "))
	count = 0
	min_range = 0
	mid_range = 50
	max_range = list(range(1, 101, 3))
	high_mid = 0
	low_mid = 0
	high_low = ""
	result = 0
	run = True
	print(max_range)

	while run:
		count += 1
		if guess == min_range:
			print("The number is " + str(min_range) + " and it took " + str(count) + " try")
		elif guess == max_range:
			print("The number is " + str(max_range) + " and it took " + str(count) + " try")
		elif guess == mid_range:
			print("The number is " + str(mid_range) + " and it took " + str(count) + " try")



		high_low = input("Is your number higher or lower than " + str(mid_range) + " : ")
		#if high_low == "higher":







	#print(search_guess(guess, max_range, mid_range, count))


	#while max_range != guess:
	#	count += 1
	#	max_range = search_guess(guess, max_range)
	#else:
	#	result = 100
	#	print("The number is: " + str(result) + " and you tried it: " + str(count))









if __name__ == '__main__':
	if sys.version_info[0] < 3:
		raise Exception("Minimum requirement: Python3")
	main()