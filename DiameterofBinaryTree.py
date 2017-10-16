#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Diameter of Binary Tree - Easy '

__author__ = 'Roger Cui'


'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
		  1
		 / \
		2   3
	   / \     
	  4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges 
between them.


Results:
Run time: beats 99.52%
Time  complex: O()
Space complex: O()
'''

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.diameter = 0

		def longest_path(sub_root):
			if not sub_root:
				return -1
			longest_left = longest_path(sub_root.left) + 1
			longest_right = longest_path(sub_root.right) + 1
			longest = max(longest_left, longest_right)
			diameter_max = longest_left + longest_right
			if diameter_max > self.diameter:
				self.diameter = diameter_max
			return longest

		longest_path(root)

		return self.diameter


if __name__ == '__main__':
	node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
	node1.left, node1.right = node2, node3
	node2.left, node2.right = node4, node5

	obj = Solution()
	result = obj.diameterOfBinaryTree(node1)
	print(result)

