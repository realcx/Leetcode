#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Best Time to Buy and Sell Stock II - Easy '

__author__ = 'Roger Cui'


'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions 
as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).


Results:
Run time: beats 18%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
			
		profit = 0
		for i in range(1, len(prices)):
			if prices[i] > prices[i-1]:
				profit += prices[i] - prices[i-1]

		return profit


if __name__ == '__main__':
	obj = Solution()
	result = obj.maxProfit([0,5,5,6,2,1,1,3])
	print(result)

