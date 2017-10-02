#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Perfect Squares - Medium '

__author__ = 'Roger Cui'


'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


Results:
Run time: ms, beats %
Time  complex: O()
Space complex: O()
'''
import math

class Solution(object):
	def numSquares(self, n):
		l = [i**2 for i in range(n) if i**2 <= n]
		
		
		# count = 0
		# if n == 0:
		# 	return 0
		# else:
		# 	m = n - int(math.sqrt(n))**2
		# 	count = self.numSquares(m)
		# 	return count + 1



if __name__ == '__main__':
	a = Solution()
	b = a.numSquares(16)
	# print(b)

