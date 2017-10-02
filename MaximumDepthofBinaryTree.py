#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Maximum Depth of Binary Tree -  easy '

__author__ = 'Roger Cui'


'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Results:
Run time: 59ms, beats 48.11%
Time  complex: O()
Space complex: O()
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		# first version
		if root == None:
			return 0
		else:
			left_count = self.maxDepth(root.left) + 1
			right_count = self.maxDepth(root.right) + 1
			max_count = max(left_count, right_count)
			return max_count

		# second version
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0

		# third version
		return max(map(self.maxDepth, [root.left, root.right])) + 1 if root else 0



if __name__ == '__main__':
	pass

