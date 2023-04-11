#!/usr/bin/python3
"""file of a write function"""

def write_file(filename="", text=""):
	"""
	function that writes a string to a text file

	Args:
		filename: name of file
		text: text to write
		Returns: no of characters written
	"""
	with open(filename, "w", encoding="utf-8") as wf:
		return wf.write(text)
