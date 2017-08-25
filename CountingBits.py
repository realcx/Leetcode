#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Counting Bits - medium'
__author__ = 'Roger Cui'

'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the 
number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it 
in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount 
in c++ or in any other language.


Results:
Run time: 178ms, beats 91%
Time  complex: O(n)
Space complex: O(n)
'''

class Solution(object):
	def countBits(self, num):

		# original method
		# arr = [0,] * (num+1)
		# for i in range(num+1):
		# 	arr[i] = str(bin(i)).count('1')
		# return arr

		# second method
		arr = [0, 1]
		while len(arr) <= num:
			tmp = map(lambda x: x + 1, arr)
			arr.extend(tmp)
		return arr[:(num+1)]



if __name__ == '__main__':
	A = Solution()
	print(A.countBits(5))


