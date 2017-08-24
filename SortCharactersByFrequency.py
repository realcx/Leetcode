#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Sort Characters By Frequency'
__author__ = 'Roger Cui'

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Results:
Run time: ms, beats 58%
Time  complex: O(n)
Space complex: O(n)
'''

from collections import Counter

class Solution(object):
	def frequencySort(self, s):
		
		# original version
		# c = Counter(s)
		# A = sorted(c.items(), key = lambda d: d[1], reverse = True)
		# B = ''
		# for v in A:
		# 	for i in range(v[1]):
		# 		B += v[0]
		# return B


		# second version
		# c = Counter(s)
		# A = sorted(c.items(), key = lambda d: d[1], reverse = True)
		# B = ''
		# for v in A:
		# 	B += v[0] * v[1]
		# return B


		# third version
		m, n = Counter(s), ''
		for v in m.most_common():
			n += v[0] * v[1]
		return n


if __name__ == '__main__':
	A = Solution()
	print(A.frequencySort("tree"))
	print(A.frequencySort("cccaaa"))
	print(A.frequencySort("Aabb"))


