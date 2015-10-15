__author__ = 'silend'

"""
Program to count partitions of number N by K summand.
Read input as "N K" from keyboard and returns number of such partitions
"""


def partition(n, k):
	if n == k or k == 1:
		numparts = 1
	elif n < k or k == 0:
		numparts = 0
	else:
		p = [1]*n
		for i in range(2,k+1):
			for m  in range(i+1,n-i+1+1):
				p[m] = p[m] + p[m-i]
				numparts = p[n-k+1]
	return numparts


def greeting():
	print("Welcome to this simple program for count partitions of number N by K summand."
			"\nPlease, enter the value of numbers in format: N K")  # format is given in a task description
	try:
		user_input = input("\n>>")
		n, k = tuple(int(x.strip()) for x in user_input.split())
	except:
		print("Please, enter correct value")
	print(partition(n, k))


greeting()