#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Delete Operation for Two Strings - Medium '

__author__ = 'Roger Cui'


'''
Given two words word1 and word2, find the minimum number of steps required to 
make word1 and word2 the same, where in each step you can delete one character 
in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make 
"eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.


Results:
Run time: beats 75.41%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		# # version 1
		# if not word1 or not word2:
		# 	ans = max(len(word1), len(word2))
		# elif word1[0] == word2[0]:
		# 	ans = self.minDistance(word1[1:], word2[1:])
		# else:
		# 	ans = 1 + min(self.minDistance(word1[1:], word2), self.minDistance(word1, word2[1:]))
		# return ans

		# version 2
		l1 = len(word1)
		l2 = len(word2)
		dp = [[0 for i in range(l1+1)] for j in range(l2+1)]
		for i in range(l1):
			for j in range(l2):
				if word1[i] == word2[j]:
					dp[j+1][i+1] = dp[j][i] + 1
				else:
					dp[j+1][i+1] = max(dp[j][i+1], dp[j+1][i])
		commom = dp[l2][l1]
		return l1 + l2 - 2 * commom
		

if __name__ == '__main__':
	obj = Solution()
	result = obj.minDistance('sea', 'eat')
	print(result)

