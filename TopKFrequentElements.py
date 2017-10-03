#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Top K Frequent Elements - Medium '

__author__ = 'Roger Cui'


'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


Results:
Run time: beats 89.13%
Time  complex: O()
Space complex: O()
'''

from collections import Counter

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		# version 1
		D = dict(Counter(nums))
		D = sorted(D, key=D.get, reverse=True)
		count = 0
		L = []

		for key in D:
			L.append(key)
			count += 1
			if count >= k:
				break

		return L

		# version 2
		L = Counter(nums).most_common(k)
		return [item[0] for item in L]
		

if __name__ == '__main__':
	obj = Solution()
	result = obj.topKFrequent([1,1,1,3,2,2], 2)
	print(result)

