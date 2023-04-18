#!/usr/bin/python3
"""file of function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
	"""
	function that appends a string at the end of a text file

	Args:
		filename: name of file
		text: text to be appended
		Returns: no of characters written
	"""
	with open(filename, "a", encoding="utf-8") as af:
		return af.write(text)
