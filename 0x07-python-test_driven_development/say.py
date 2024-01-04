#!/usr/bin/python3
class Name:
	def say_my_name(self,first_name, last_name=""):
		if not isinstance(first_name,str):
			raise TypeError("first_name must be a string or last_name must be a string")
		if not isinstance(last_name,str):
			raise TypeError("first_name must be a string or last_name must be a string")
		print(f"My name is {first_name} {last_name}")

