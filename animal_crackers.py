"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

def animal_crackers(str):

	str = str.lower()

	str = str.split()

	if str[0][0] == str[1][0]:

		return True

	else:

		return False