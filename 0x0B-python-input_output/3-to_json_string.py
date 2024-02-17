#!/usr/bin/python3
"""file of function that returns the JSON representation of an object"""
import json

def to_json_string(my_obj):
	"""
	function that returns the JSON representation of an object
	Args:
		my_obj: object
		Returns: JSON representation of the object
	"""
	return json.dumps(my_obj)
