"""
Find e to the Nth Digit - Just like the previous problem, but with e instead of π (pi). Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
"""

import math 

nums = int(input("How many spaces?: "))

while nums > 1000:

	print("Num too large: ")

	nums = int(raw_input("How many spaces"))

else:
	print("%.*f"%(nums,math.e))