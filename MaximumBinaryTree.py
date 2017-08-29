#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Maximum Binary Tree - Medium '

__author__ = 'Roger Cui'


'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

	  6
	/   \
   3     5
	\    / 
	 2  0   
	   \
		1
Note:
The size of the given array will be in the range [1,1000].


Results:
Run time: 212ms, beats 72.13%
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
	def constructMaximumBinaryTree(self, nums):
		# first try
		l = len(nums)
		if l == 1:
			return TreeNode(nums[0])
		else:
			maxnum = max(nums)
			maxidx = nums.index(maxnum)
			node = TreeNode(maxnum)
			node.left = self.constructMaximumBinaryTree(nums[:maxidx]) if maxidx != 0 else None
			node.right = self.constructMaximumBinaryTree(nums[maxidx+1:]) if maxidx != l-1 else None
			return node


if __name__ == '__main__':
	Solution().constructMaximumBinaryTree([3,2,1,6,0,5])

