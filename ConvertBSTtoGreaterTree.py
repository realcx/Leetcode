#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Convert BST to Greater Tree - Easy '

__author__ = 'Roger Cui'


'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key 
of the original BST is changed to the original key plus sum of all keys greater 
than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
			  5
			/   \
		   2     13

Output: The root of a Greater Tree like this:
			 18
			/   \
		  20     13
		  

Results:
Run time: beats 24.95%
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
	def convertBST(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		self.val = 0
		def visit(root):
			if root:
				visit(root.right)
				root.val += self.val
				self.val = root.val
				visit(root.left)
		visit(root)

		return root


if __name__ == '__main__':
	node1 = TreeNode(5)
	node2, node3 = TreeNode(2), TreeNode(13)
	node1.left, node1.right = node2, node3

	def print_treenode(root):
		if root != None:
			print(root.val)
			print_treenode(root.left)
			print_treenode(root.right)

	print_treenode(node1)

	obj = Solution()
	node11 = obj.convertBST(node1)
	print_treenode(node1)

