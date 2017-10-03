#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Majority Element - Easy '

__author__ = 'Roger Cui'


'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always 
exist in the array.


Results:
Run time: beats 38%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return collections.Counter(nums).most_common(1)[0][0]



if __name__ == '__main__':


