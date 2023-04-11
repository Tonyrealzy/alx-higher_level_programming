#!/usr/bin/python3
"""file of a function that reads a textfile"""


def read_file(filename=""):
	"""
	function that reads a textfile
	"""
	with open(filename, "r", encoding="utf-8") as rf:
		print(rf.read(), end="")
