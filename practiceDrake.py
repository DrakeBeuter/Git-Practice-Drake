
#partner 1 name: Drake
#partner 2 name: Nic
###############################################################################
#This function generates 10 random numbers and returns the product of those 10 numbers.
import random as rand
import numpy as np
def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
	l = []
	for i in range(n):
		l.append(rand.randint(1,10))
	return l

def multiplyRandom(numbers):
	'''takes in a list of n numbers and returns the product of the numbers'''
	return np.prod(numbers)

def main():
	print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
	main()
