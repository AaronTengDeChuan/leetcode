#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: Void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) - 1):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix) / 2):
            for j in range(len(matrix)):
                matrix[j][i], matrix[j][len(matrix) - i - 1] = matrix[j][len(matrix) - i - 1], matrix[j][i]



solution = Solution()
matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
solution.rotate(matrix)
for i in range(len(matrix)):
    print matrix[i]
