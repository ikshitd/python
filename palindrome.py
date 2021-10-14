def palindrome(str):

	str = str.replace(" ","")

	str = str.lower()

	if str == str[::-1]:

		return True 

	else:
	
	    return False	