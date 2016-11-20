#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        startx = 0
        starty = -1
        result = []
        rows = len(matrix)
        if rows == 0:
            return result
        cols = len(matrix[0])
        visitedRows = 0
        visitedCols = 0
        #方向数组
        x = [1,0,-1,0]
        y = [0,1,0,-1]
        #0:right  1:down 2:left 3:up
        direct = 0
        while True:
            step = 0
            if x[direct] == 0:
                step = rows - visitedRows
            else:
                step = cols - visitedCols
            if step == 0:
                break
            for i in range(step):
                startx += y[direct]
                starty += x[direct]
                result.append(matrix[startx][starty])
            if x[direct] != 0:
                visitedRows += 1
            if y[direct] != 0:
                visitedCols += 1
            direct += 1
            direct %= 4
        return result

solution = Solution()
matrix = []
print solution.spiralOrder(matrix)



