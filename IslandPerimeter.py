#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Island Perimeter - Easy '

__author__ = 'Roger Cui'


'''
You are given a map in form of a two-dimensional integer grid where 1 represents 
and and 0 represents water. Grid cells are connected horizontally/vertically 
(not diagonally). The grid is completely surrounded by water, and there is 
exactly one island (i.e., one or more connected land cells). The island doesn't 
have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height 
don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16


Results:
Run time: beats 76.8%
Time  complex: O()
Space complex: O()
'''

class Solution(object):
	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		row = len(grid)
		col = len(grid[0])
		perimeter = 0

		# pad
		for i in range(row):
			grid[i].insert(0, 0)
			grid[i].append(0)
		grid.insert(0, [0 for i in range(col+2)])
		grid.append([0 for i in range(col+2)])

		# count
		for i in range(1, row+1):
			for j in range(1, col+1):
				if grid[i][j] == 1:
					perimeter += 4 - (grid[i-1][j] + grid[i+1][j] + grid[i][j-1] + grid[i][j+1])
		
		return perimeter


if __name__ == '__main__':
	obj = Solution()
	grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
	result = obj.islandPerimeter(grid)
	print(result)

