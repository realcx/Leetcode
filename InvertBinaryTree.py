#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Invert Binary Tree - Easy '

__author__ = 'Roger Cui'


'''
Invert a binary tree.

	 4
   /   \
  2     7
 / \   / \
1   3 6   9
to
	 4
   /   \
  7     2
 / \   / \
9   6 3   1


Results:
Run time: beats 29.44%
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
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if root != None:
			root.right, root.left = root.left, root.right
			self.invertTree(root.left)
			self.invertTree(root.right)
			return root


if __name__ == '__main__':
	node1 = TreeNode(4)
	node2, node3 = TreeNode(2), TreeNode(7)
	node4, node5, node6, node7 = TreeNode(1), TreeNode(3), TreeNode(6), TreeNode(9)
	node1.left, node1.right = node2, node3
	node2.left, node2.right = node4, node5
	node3.left, node3.right = node6, node7

	def print_treenode(root):
		if root != None:
			print(root.val)
			print_treenode(root.left)
			print_treenode(root.right)

	print_treenode(node1)

	obj = Solution()
	obj.invertTree(node1)
	print_treenode(node1)


