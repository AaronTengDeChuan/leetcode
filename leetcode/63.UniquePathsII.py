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
                    obstacleGird[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGird[i][j] = 1
                elif i == 0:
                    obstacleGird[i][j] = obstacleGird[i][j - 1]
                elif j == 0:
                    obstacleGird[i][j] = obstacleGird[i - 1][j]
                else:
                    if obstacleGird[i][j] == 1:
                        obstacleGird[i][j] = 0
                    else:
                        obstacleGird[i][j] = obstacleGird[i - 1][j] + obstacleGird[i][j - 1]
        return obstacleGird[i][j]

solution = Solution()
obstacleGird = [[1,0]]
print solution.uniquePathsWithObstacles(obstacleGird)
