"""
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

nums = int(input("How many terms : "))

n1 , n2 = 0,1
count = 0

while nums <=0:
	print("Please enter a positive number: ")
	if nums <= 0:
		nums = int(input("How many terms : "))

if nums == 1:
	print("Fibonacci sequence :")
	print(n1)

else:
	print("Fibonacci sequence :")
	while count < nums:
		print(n1)
		nth = n1 + n2
		count += 1

		n1 = n2
		n2 = nth