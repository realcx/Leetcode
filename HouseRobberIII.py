#!usr/bin/env python3
# -*- coding: utf-8 -*-

' House Robber III - Medium '

__author__ = 'Roger Cui'


'''
The thief has found himself a new place for his thievery again. There is only one 
entrance to this area, called the "root." Besides the root, each house has one 
and only one parent house. After a tour, the smart thief realized that "all houses 
in this place forms a binary tree". It will automatically contact the police if 
two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting 
the police.

Example 1:
	 3
	/ \
   2   3
	\   \ 
	 3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
	 3
	/ \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.


Results:
Run time: beats 82.45%
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
	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		# # version 1
		# def sub_rob(sub_root, is_rob):
		# 	if not sub_root:
		# 		return 0
		# 	if is_rob:
		# 		return sub_rob(sub_root.left, False) + sub_rob(sub_root.right, False) + sub_root.val
		# 	else:
		# 		sub_rob1 = sub_rob(sub_root.left, True) + sub_rob(sub_root.right, True)
		# 		sub_rob2 = sub_rob(sub_root.left, False) + sub_rob(sub_root.right, False)
		# 		sub_rob3 = sub_rob(sub_root.left, True) + sub_rob(sub_root.right, False)
		# 		sub_rob4 = sub_rob(sub_root.left, False) + sub_rob(sub_root.right, True)
		# 		return max(sub_rob1, sub_rob2, sub_rob3, sub_rob4)
		# return max(sub_rob(root, True), sub_rob(root, False))

		# version 2
		def sub_rob(sub_root):
			if not sub_root:
				return (0, 0)
			left_rob = sub_rob(sub_root.left)
			right_rob = sub_rob(sub_root.right)
			rob_now = left_rob[1] + right_rob[1] + sub_root.val
			rob_later = max(left_rob) + max(right_rob)
			return (rob_now, rob_later)

		return max(sub_rob(root))


if __name__ == '__main__':
	node1, node2, node3 = TreeNode(3), TreeNode(4), TreeNode(5)
	node4, node5, node6 = TreeNode(1), TreeNode(3), TreeNode(1)
	node1.left, node1.right = node2, node3
	node2.left, node2.right = node4, node5
	node3.right = node6

	obj = Solution()
	result = obj.rob(node1)
	print(result)

