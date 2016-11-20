#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        water = 0
        while left < right - 1 and height[left] <= height[left + 1]:
            left += 1
        while right >left + 1 and height[right] <=height[right - 1]:
            right -= 1
        while left < right:
            l = height[left]
            r = height[right]
            if l < r:
                while left < right and height[left] <= l:
                    water += l - height[left]
                    left += 1
            else:
                while left < right and height[right] <= r:
                    water += r - height[right]
                    right -= 1
        return water

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print solution.trap(height)

