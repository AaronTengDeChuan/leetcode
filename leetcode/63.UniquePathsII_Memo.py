#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGird):
        """
        :type obstacleGird: List[List[int]]
        :rtype: int
        """
        if len(obstacleGird) == 0:
            return 0
        for i in range(len(obstacleGird)):
            for j in range(len(obstacleGird[0])):
                if obstacleGird[i][j] == 1:
                    obstacleGird[0][j] = 0
                elif j == 0:
                    if i == 0:
                        obstacleGird[i][j] = 1
                else:
                    obstacleGird[0][j] += obstacleGird[0][j - 1]
        return obstacleGird[0][j]

solution = Solution()
obstacleGird = [[1,0]]
print solution.uniquePathsWithObstacles(obstacleGird)
