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

solution = Solution()
heights = [4,2,0,3,2,5]
print solution.largestRectangleArea(heights)
                
            

        
