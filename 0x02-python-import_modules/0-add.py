#!/usr/bin/python3
"""a program to import a function that adds two number and prints the output as well"""
if __name__ == "__main__":
	from add_0 import add
	a = 1
	b = 2
	add(a,b)
	print("{} + {} = {}".format(a,b, add(a,b)))
