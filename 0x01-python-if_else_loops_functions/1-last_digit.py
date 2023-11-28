#!/usr/bin/python3
"""a program that prints the last digits of a number."""
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if (ld < 0):
	ld *= -1 
if(ld > 5):
	print(f"Last digit of {number} is {ld} and is greater than 5")
elif(ld == 0):
	print(f"Last digit of {number} is {ld} and is 0")
else:
	print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
