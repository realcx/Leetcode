#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Reverse String - easy '

__author__ = 'Roger Cui'


'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Results:
Run time: 36ms, beats 95.47%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]



if __name__ == '__main__':
	pass

