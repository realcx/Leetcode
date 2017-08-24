#!usr/bin/env python3
# -*- coding: utf-8 -*-

'Judge Route Circle - easy'

__author__ = 'Roger Cui'

'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false


Results:
Run time: , beats 
Time complex:
Space complex:
'''

class Solution(object):
	def judgeCircle(self, moves):
		
		# method 1
		# c = collections.Counter(moves)
		# if c['U'] == c['D'] and c['R'] == c['L']:
		#     return True
		# else:
		#     return False
		
		# method 2
		if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
			return True
		else:
			return False