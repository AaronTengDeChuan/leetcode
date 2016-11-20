#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    if i != 0:
                        grid[0][j] += grid[i][j]
                elif i == 0:
                    grid[0][j] += grid[0][j - 1]
                else:
                    if grid[0][j - 1] > grid[0][j]:
                        grid[0][j] += grid[i][j]
                    else:
                        grid[0][j] = grid[i][j] + grid[0][j - 1]
        return grid[0][j]

solution = Solution()
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print solution.minPathSum(grid)

