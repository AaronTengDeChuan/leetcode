#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def jump(self, nums):
        curMax = 0
        curLen = 0
        step = 0
        for i in range(len(nums)):
            if curLen < i:
                step += 1
                curLen = curMax
            curMax = max(curMax, nums[i] + i)
        return step

solution = Solution()
nums = [1,2,3,1,1,1,2,1,1,0]
print solution.jump(nums)
