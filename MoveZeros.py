#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Move Zeroes - easy '

__author__ = 'Roger Cui'


'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


Results:
Run time: beats 49.47%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		# first version
		idx = 0
		L = len(nums)
		for i in range(L):
			if nums[i] != 0:
				nums[idx] = nums[i]
				idx += 1
		nums[idx:] = [0 for i in range(L - idx)]


if __name__ == '__main__':
	obj = Solution()
	nums = [1,0,1,2,4]
	obj.moveZeroes(nums)
	print(nums)

