def pangram(str):

	import string 

	alphabet = string.ascii_lowercase

	str = str.replace(" ","")

	str = str.lower()

	if set(str) == set(alphabet):

		return True

	else:

		return False