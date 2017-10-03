#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Excel Sheet Column Number - Easy '

__author__ = 'Roger Cui'


'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

	A -> 1
	B -> 2
	C -> 3
	...
	Z -> 26
	AA -> 27
	AB -> 28 


Results:
Run time: beats 54.26%
Time  complex: O(n)
Space complex: O(1)
'''
from functools import reduce

class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# version 1
		def changeToNumber(s):
			return ord(s) - ord('A') + 1
		# change character to number
		num = list(map(changeToNumber, s))
		# combine into single number
		L = len(s)
		result = 0
		for i in range(L):
			result += num[L-i-1] * (26**i)
		return result

		# version 2
		num = map(lambda x: ord(x) - ord('A') + 1, s)
		num = reduce(lambda a, b: 26 * a + b, num)
		return num


if __name__ == '__main__':
	obj = Solution()
	result = obj.titleToNumber('AA')
	print(result)

