#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Valid Anagram - Easy '

__author__ = 'Roger Cui'


'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.


Results:
Run time: beats 41.9%
Time  complex: O()
Space complex: O()
'''
from collections import Counter

class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		# version 1
		s_dict = Counter(s)
		t_dict = Counter(t)
		# different length
		if len(s_dict) != len(t_dict):
			return False
		# different elements and numbers
		for k, v in s_dict.items():
			if t_dict.get(k) == None:
				return False
			if t_dict[k] != v:
				return False
		return True

		# version 2
		return sorted(s) == sorted(t)



if __name__ == '__main__':
	obj = Solution()
	result = obj.isAnagram('anagram', 'nagarame')
	print(result)

