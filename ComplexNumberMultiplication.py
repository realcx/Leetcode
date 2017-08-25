#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Complex Number Multiplication - medium'
__author__ = 'Roger Cui'

'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
1.The input strings will not have extra blank.
2.The input strings will be given in the form of a+bi, where the integer a and b will both belong to the 
range of [-100, 100]. And the output should be also in this form.


Results:
Run time: 36ms, beats 47%
Time  complex: O(n)
Space complex: O(n)
'''

class Solution(object):
	def complexNumberMultiply(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		# original method
		# a = a.split('+')
		# n1 = int(a[0])
		# m1 = int(a[1].split('i')[0])
		# b = b.split('+')
		# n2 = int(b[0])
		# m2 = int(b[1].split('i')[0])
		# return str(n1*n2 - m1*m2) + '+' + str(n1*m2 + n2*m1) + 'i'

		# second method
		n1, m1 = map(int, a[:-1].split('+'))
		n2, m2 = map(int, b[:-1].split('+'))
		return str(n1*n2 - m1*m2) + '+' + str(n1*m2 + n2*m1) + 'i'


if __name__ == '__main__':
	A = Solution()
	print(A.complexNumberMultiply('1+1i', '1+1i'))
	print(A.complexNumberMultiply('1+-1i', '1+-1i'))


