#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curMax = 0
        curStep = 0
        for i in range(len(nums)):
            curMax = max(curMax, nums[i] + i)
            if curMax <= i and curMax != len(nums) - 1:
                return False
        return True

solution = Solution()
nums = [3,2,1,0,4]
print solution.canJump(nums)
