#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Find the Duplicate Number - Medium '

__author__ = 'Roger Cui'


'''
Given an array nums containing n + 1 integers where each integer is between 1 and 
n (inclusive), prove that at least one duplicate number must exist. Assume that 
there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more 
than once.


Results:
Run time: beats %
Time  complex: O()
Space complex: O()
'''
import collections

class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# version 1
		D = dict(collections.Counter(nums))
		for k, v in D.items():
			if v > 1:
				return k



if __name__ == '__main__':
	obj = Solution()
	result = obj.findDuplicate([1,2,3,2])
	print(result)

