#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Single Number - easy '

__author__ = 'Roger Cui'


'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Results:
Run time: 46ms, beats 52.5%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		result = nums[0]
		for i in range(1, len(nums)):
			result ^= nums[i]
		return result



if __name__ == '__main__':
	obj = Solution()
	result = obj.singleNumber([1,2,3,2,1])
	print(result)

