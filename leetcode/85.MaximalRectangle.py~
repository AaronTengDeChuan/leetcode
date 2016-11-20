#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        heights.append(0)
        stack = []
        min = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                tmp = stack.pop()
                area = 0
                if len(stack) == 0:
                    area += (tmp + 1) * heights[tmp]
                else:
                    area += (tmp - stack[-1]) * heights[tmp]
                area += (i - tmp - 1) * heights[tmp]
                if area > min:
                    min = area
            stack.append(i)  
        return min

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        max = 0
        heights = []
        for i in range(len(matrix[0])):
            heights.append(0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            tmp = self.largestRectangleArea([k for k in heights])
            if max < tmp:
                max = tmp
        return max

solution = Solution()
matrix = [
    "10100",
    "10111",
    "11111",
    "10010",
]
print solution.maximalRectangle(matrix)

        
