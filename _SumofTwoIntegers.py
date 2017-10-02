#!usr/bin/env python3
# -*- coding: utf-8 -*-

'  -  '

__author__ = 'Roger Cui'


'''


Results:
Run time: ms, beats %
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		return self.getSum((a & b) << 1, a ^ b) if a != 0 else b



if __name__ == '__main__':
	obj = Solution()
	result = obj.getSum(3, -3)
	print(result)

