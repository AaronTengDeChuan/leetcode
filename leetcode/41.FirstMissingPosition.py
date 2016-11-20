#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type num: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 1
        for i in range(size):
            while nums[i] != i + 1:
                if nums[i] >= size or nums[i] <= 0 or nums[i] == nums[nums[i] - 1]:
                    break
                temp = nums[i]
                nums[i], nums[temp - 1] = nums[temp - 1], nums[i]
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        else:
            return i + 2

solution = Solution()
nums = [3,4,-1,1]
print solution.firstMissingPositive(nums)
