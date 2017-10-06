#!usr/bin/env python3
# -*- coding: utf-8 -*-

' First Unique Character in a String - Easy '

__author__ = 'Roger Cui'


'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


Results:
Run time: beats 31.4%
Time  complex: O()
Space complex: O()
'''
from collections import Counter

class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# # version 1
		# if not s:
		# 	return -1
		
		# for i in range(len(s)):
		# 	if i == 0:
		# 		if s[i] not in s[i+1:]:
		# 			return i
		# 	elif i == len(s) - 1:
		# 		if s[i] not in s[:i]:
		# 			return i
		# 		else:
		# 			return -1
		# 	elif s[i] not in s[i+1:] and s[i] not in s[:i]:
		# 		return i


		# version 2
		S = dict(Counter(s))
		l = []
		for k, v in S.items():
			if v == 1:
				l.append(s.find(k))

		if l:
			return min(l)
		else:
			return -1


if __name__ == '__main__':
	obj = Solution()
	result = obj.firstUniqChar('leetcode')
	print(result)

