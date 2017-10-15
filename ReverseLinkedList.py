#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Reverse Linked List - Easy '

__author__ = 'Roger Cui'


'''
Reverse a singly linked list.


Results:
Run time: beats 72.75%
Time  complex: O()
Space complex: O()
'''

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		prev_head = None
		while head:
			tmp = head.next
			head.next = prev_head
			prev_head = head
			head = tmp

		return prev_head


if __name__ == '__main__':
	list1, list2, list3 = ListNode(1), ListNode(2), ListNode(3)
	list1.next = list2
	list2.next = list3

	def print_list(l):
		head = l
		while head:
			print(head.val)
			head = head.next

	print_list(list1)

	obj = Solution()
	result = obj.reverseList(list1)

	print_list(result)



