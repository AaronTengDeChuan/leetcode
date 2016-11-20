#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anythong, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        row_flag = False
        col_flag = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_flag = True
                    if j == 0:
                        col_flag = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for i in range(1,n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
        if row_flag:
            for i in range(n):
                matrix[0][i] = 0
        if col_flag:
            for i in range(m):
                matrix[i][0] = 0

solution = Solution()
matrix = [
    [1,1,0,1],
    [1,2,2,1],
    [-1,0,1,1],
    [1,1,1,1]
]
solution.setZeroes(matrix)
for i in matrix:
    print i
