#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Binary Tree Inorder Traversal - Medium '

__author__ = 'Roger Cui'


'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
	\
	 2
	/
   3
return [1,3,2].


Results:
Run time: beats 48.22%
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
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []

		L = self.inorderTraversal(root.left)
        L.append(root.val)
        R = self.inorderTraversal(root.right)
        return L + R



if __name__ == '__main__':
	obj = Solution()
	root = TreeNode(1)
	a = TreeNode(2)
	b = TreeNode(3)
	root.right = a
	a.left = b

	result = obj.inorderTraversal(root)
	print(result)

