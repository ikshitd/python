"""
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
"""
import math 

precision =  int(input("How many spaces?"))

while precision > 50:
	print("Number too large")
	precision = int(raw_input("How many spaces? "))

else:
	print("%.*f"%(precision,math.pi))




