#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[len(nums) - 1] = 0
        for i in range(len(nums) - 2, -1, -1):
            min_step = nums[i + 1]
            for j in range(i + 1, min(nums[i] + i, len(nums) - 1) + 1):
                if nums[j] < min_step:
                    min_step = nums[j]
            nums[i] = min_step + 1
        return nums[0]

solution = Solution()
nums = [1,2,3,1,1,1,2,1,1,0]
print solution.jump(nums)
