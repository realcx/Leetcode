#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'#617 Merge Two Binary Tree - easy'

__author__ = 'Roger Cui'

"""
Given two binary trees and imagine that when you put one of them to cover the 
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two 
nodes overlap, then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
		  1                         2                             
		 / \                       / \                            
		3   2                     1   3                        
	   /                           \   \                      
	  5                             4   7                  
Output: 
Merged tree:
		 3
		/ \
	   4   5
	  / \   \ 
	 5   4   7

Note: The merging process must start from the root nodes of both trees.

Results:
Run time: beats 80%
Time  complex: O(n)
Space complex: O(n)
"""

class TreeNode(object):
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None


class Solution(object):
	def mergeTrees(self, t1, t2):

		# original method
		if not t1 and not t2:
			return None
		else:
			t3 = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
			t3.left  = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
			t3.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
			return t3

		# second method
		if not t1 and not t2:
			return None
		if not t1:
			return t2
		if not t2:
			return t1
		else:
			t3 = TreeNode(t1.val + t2.val)
			t3.left  = self.mergeTrees(t1.left,  t2.left)
			t3.right = self.mergeTrees(t1.right, t2.right)
			return t3


if __name__ = '__main__':


