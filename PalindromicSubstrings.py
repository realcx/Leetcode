#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Palindromic Substrings - Medium '

__author__ = 'Roger Cui'


'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as 
different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.


Results:
Run time: beats 20.1%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def countSubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		n = len(s)
		count = 0
		for i in range(n):
			for j in range(n-i):
				tmp = s[j:j+i+1]
				if tmp == tmp[::-1]:
					count += 1
		return count


if __name__ == '__main__':
	obj = Solution()
	result = obj.countSubstrings('aaa')
	print(result)

