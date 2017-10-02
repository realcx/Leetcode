#!usr/bin/env python3
# -*- coding: utf-8 -*-

'  -  '

__author__ = 'Roger Cui'


'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
	"1",
	"2",
	"Fizz",
	"4",
	"Buzz",
	"Fizz",
	"7",
	"8",
	"Fizz",
	"Buzz",
	"11",
	"Fizz",
	"13",
	"14",
	"FizzBuzz"
]


Results:
Run time: 65ms, beats 97.64%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		L = [str(i+1) for i in range(n)]
		for i in range(1, n+1):
			if i % 15 == 0:
				L[i-1] = 'FizzBuzz'
			elif i % 3 == 0:
				L[i-1] = 'Fizz'
			elif i % 5 == 0:
				L[i-1] = 'Buzz'

		return L


if __name__ == '__main__':
	obj = Solution()
	result = obj.fizzBuzz(15)
	print(result)

