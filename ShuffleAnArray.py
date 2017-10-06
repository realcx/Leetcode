#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Shuffle an Array - Medium '

__author__ = 'Roger Cui'


'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();


Results:
Run time: beats 14.8%
Time  complex: O()
Space complex: O()
'''
import random

class Solution(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		

	def reset(self):
		"""
		Resets the array to its original configuration and return it.
		:rtype: List[int]
		"""
		return self.nums
		

	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		:rtype: List[int]
		"""
		# # version 1
		# arr = self.nums[:]
		# result = [None for i in range(len(self.nums))]
		# for i in range(len(self.nums)):
		# 	if arr:
		# 		idx = random.randint(0, len(arr) - 1)
		# 		result[i] = arr[idx]
		# 		arr.pop(idx)

		# return result


		# version 2
		arr = self.nums[:]
		L = len(arr)
		for i in range(L):
			j = random.randint(0, L-1)
			arr[i], arr[j] = arr[j], arr[i]

		return arr



if __name__ == '__main__':
	obj = Solution([1,2,3,4,5])
	print(obj.reset())
	print(obj.shuffle())

