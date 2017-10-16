#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Permutations - Medium '

__author__ = 'Roger Cui'


'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


Results:
Run time: beats 65.98%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.result = []

		def func(p, l):
			if len(l) == 1:
				p += l
				self.result += p,
			else:
				n = len(l)
				for i in range(n):
					m = l.copy()
					m.pop(i)
					func(p + [l[i]], m)
				
		func([], nums)

		return self.result



if __name__ == '__main__':
	obj = Solution()
	result = obj.permute([1,2,3])
	print(result)

