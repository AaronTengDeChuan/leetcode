#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def indexToPos(self, n, index):
        i = index / n
        j = index % n
        return i, j
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) / 2
            i, j = self.indexToPos(n, mid)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

solution = Solution()
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
]
target = int(raw_input("target = "))
print solution.searchMatrix(matrix, target)

