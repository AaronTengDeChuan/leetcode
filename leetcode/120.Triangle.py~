#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def minimumTotal(self, triangle):
        length = len(triangle[-1])
        for i in range(len(triangle) - 2, -1, -1):
            length -= 1
            for j in range(length):
                if triangle[i + 1][j] < triangle[i + 1][j + 1]:
                    triangle[i][j] += triangle[i + 1][j]
                else:
                    triangle[i][j] += triangle[i + 1][j + 1]
        return triangle[0][0]

    def minimumTotal_top_to_bottom(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
            triangle[i][-1] += triangle[i - 1][-1]
        min_sum = triangle[-1][0]
        for i in triangle[-1]:
            if min_sum > i:
                min_sum = i
        return min_sum

solution = Solution()
triangle = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
print solution.minimumTotal(triangle)
        
