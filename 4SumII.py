#!usr/bin/env python3
# -*- coding: utf-8 -*-

' 4Sum II - Medium '

__author__ = 'Roger Cui'


'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


Results:
Run time: beats 51%
Time  complex: O(n^2)
Space complex: O()
'''
from collections import Counter

class Solution(object):
	def fourSumCount(self, A, B, C, D):
		"""
		:type A: List[int]
		:type B: List[int]
		:type C: List[int]
		:type D: List[int]
		:rtype: int
		"""
		# # version 1
		# count = 0
		# N = len(A)
		# for i in range(N):
		# 	for j in range(N):
		# 		for k in range(N):
		# 			for l in range(N):
		# 				if A[i] + B[j] + C[k] + D[l] == 0:
		# 					count += 1
		# return count


		# # version 2
		# Al = dict(Counter(A))
		# Bl = dict(Counter(B))
		# Cl = dict(Counter(C))
		# Dl = dict(Counter(D))
		# AB, CD = {}, {}
		# for A_key, A_value in Al.items():
		# 	for B_key, B_value in Bl.items():
		# 		if A_key + B_key not in AB:
		# 			AB[A_key + B_key] = A_value * B_value
		# 		else:
		# 			AB[A_key + B_key] += A_value * B_value
					
		# for C_key, C_value in Cl.items():
		# 	for D_key, D_value in Dl.items():
		# 		if C_key + D_key not in CD:
		# 			CD[C_key + D_key] = C_value * D_value
		# 		else:
		# 			CD[C_key + D_key] += C_value * D_value

		# count = 0
		# for AB_key, AB_value in AB.items():
		# 	for CD_key, CD_value in CD.items():
		# 		if AB_key + CD_key == 0:
		# 			count += AB_value * CD_value
					
		# return count


		# # version 3 
		# AB = [a + b for a in A for b in B]
		# CD = [c + d for c in C for d in D]
		# AB = dict(Counter(AB))
		# CD = dict(Counter(CD))

		# count = 0
		# for AB_key, AB_value in AB.items():
		# 	for CD_key, CD_value in CD.items():
		# 		if AB_key + CD_key == 0:
		# 			count += AB_value * CD_value

		# return count


		# version 4
		AB = [a + b for a in A for b in B]
		AB = dict(Counter(AB))

		count = 0
		for c in C:
			for d in D:
				if -c - d in AB:
					count += AB[-c-d]

		return count
		


if __name__ == '__main__':
	obj = Solution()
	A = [-1,-1]
	B = [-1,1]
	C = [-1,1]
	D = [1,-1]
	result = obj.fourSumCount(A, B, C, D)
	print(result)

