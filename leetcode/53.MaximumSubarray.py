#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        pre_sum = nums[0]
        for i in range(1,len(nums)):
            if pre_sum <= 0:
                pre_sum = nums[i]
            else:
                pre_sum += nums[i]
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum

solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print solution.maxSubArray(nums)

