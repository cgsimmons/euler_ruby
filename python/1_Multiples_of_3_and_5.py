#!/usr/bin/python
"""Find the sum of all the multiples of 3 or 5 below 1000.
"""

if __name__ == "__main__":
	sum = 0
	for i in range(1000):
		if i%3 == 0 or i%5 == 0:
			sum = sum + i

	print sum
			
