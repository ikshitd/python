"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""

#WHAT MAKES THIS PROBLEM AMAZING IS THAT INSTEAD OF THINKING ABOUT THE EXISTENCE OF 6 AND 9 , JUST THINK OF UNTIL I DON'T GET A 6 JUST KEEP ADDING THE NUM AND SO ON FOR 9 AS WELL

def summer_69(list):

	total = 0
	add = True

	for num in list:

		while add:

			if num != 6:

				total += num

				break 
			
			else:

				add = False
		while not add:
		
			if num != 9:

				break
			else:
			
				add = True 

				break 
	return total			
			
