#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'#461 Hamming distance - easy'

__author__ = 'Roger Cui'


"""
The Hamming distance between two integers is the number of positions at which 
the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
	   ?   ?
The above arrows point to positions where the corresponding bits are different.

Results:
Run time: 32ms, beat 82%
Time  complex: O(1)
Space complex: O(1)
"""

class Solution(object):
	"""
	:type x: int
	:type y: int
	:rtype: int
	"""
	def hammingDistance(self, x, y):
		count = 0
		m = bin(x^y)
		n = len(m)
		for i in range(2,n):
			if m[i] == '1':
				count = count + 1
				
		return count


if __name__=='__main__':
	s = Solution()
	s.hammingDistance(1,4)

	