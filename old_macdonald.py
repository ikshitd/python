"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald

Note: 'macdonald'.capitalize() returns 'Macdonald'
"""

def old_macdonald(str):

	first_half = str[0:3]

	second_half = str[3:]

	return first_half.capitalize() + second_half.capitalize()

