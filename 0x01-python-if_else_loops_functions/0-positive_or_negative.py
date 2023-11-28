#!/usr/bin/python3
"""a program checks if a number is positive or negative"""
import random
number = random.randint(-10, 10)
if(number >= 0):
	print(f"{number} is positive")
elif(number == 0):
	print(f"{number} is zero")
else:
	print(f"{number} is negative")
