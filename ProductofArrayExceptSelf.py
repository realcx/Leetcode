#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Product of Array Except Self - Medium '

__author__ = 'Roger Cui'


'''
Given an array of n integers where n > 1, nums, return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? 
(Note: The output array does not count as extra space for the purpose of 
space complexity analysis.)


Results:
Run time: beats 37.79%
Time  complex: O(n)
Space complex: O(n)
'''

class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		L = len(nums)
		result = [0 for i in range(L)]

		# forward multiply without itself
		tmp = 1
		for i in range(L):
			result[i] = tmp
			tmp = tmp * nums[i]

		# backward multiply without itself
		tmp = 1
		for i in range(L-1, -1, -1):
			result[i] = tmp * result[i]
			tmp = tmp * nums[i]
			
		return result


if __name__ == '__main__':
	obj = Solution()
	result = obj.productExceptSelf([1,2,3,4])
	print(result)

