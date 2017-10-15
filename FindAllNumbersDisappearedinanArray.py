#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Find All Numbers Disappeared in an Array - Easy '

__author__ = 'Roger Cui'


'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


Results:
Run time: beats 38.21%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		a = set(nums)
		b = [i+1 for i in range(len(nums))]
		b = set(b)
		c = b - a & b
		return list(c)


if __name__ == '__main__':
	obj = Solution()
	result = obj.findDisappearedNumbers([4,3,2,7,8,2,3,1])
	print(result)

