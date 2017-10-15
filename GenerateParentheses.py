#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Generate Parentheses - Medium '

__author__ = 'Roger Cui'


'''
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


Results:
Run time: beats 29.42%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		self.L = []

		def generate(s, left, right):
			if left:
				generate(s + '(', left-1, right)
			if right > left:
				generate(s + ')', left, right-1)
			if left == 0 and right == 0:
				self.L += s,

		generate('', n, n)

		return self.L



if __name__ == '__main__':
	obj = Solution()
	result = obj.generateParenthesis(3)
	print(result)

