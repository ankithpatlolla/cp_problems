# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.


def num_count (n):
	count = 0
	while n:
		n = n // 10
		count += 1
	return count	
def isrotation(x, y):
	# Your code goes here
	digits = num_count(x)
	expo = 10 ** (digits - 1)
	for i in range(digits):
		rem = x // expo
		rotation = ((x * 10) + rem) - (rem * expo)

	pass