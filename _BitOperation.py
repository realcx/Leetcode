def count_one(n):
	count = 0
	while n:
		n = n & (n - 1)
		count += 1
	return count


# Use ^ to remove even exactly same numbers and save the odd, 
# or save the distinct bits and remove the same.
def getSum(a, b):
	sum = a
	while b != 0:
		sum = a ^ b 		# calculate sum of a and b without thinking the carry 
		b = (a & b) << 1 	# calculate the carry
		a = sum  			# add sum(without carry) and carry
	
	return sum

