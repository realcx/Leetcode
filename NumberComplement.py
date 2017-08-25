#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Number Complement - easy'
__author__ = 'Roger Cui'

'''
Given a positive integer, output its complement number. The complement strategy is to flip the 
bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement 
is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement 
is 0. So you need to output 0.


Results:
Run time: 29ms, beats 96%
Time  complex: O(n)
Space complex: O(n)
'''

class Solution(object):
	def findComplement(self, num):

		# original method
		i = 1
		while i <= num:
			num = num ^ i
			i = i << 1
		return num


if __name__ == '__main__':
	A = Solution()
	print(A.findComplement(5))


