#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = 1
        max = len(nums) - 1
        while min < max:
            cnt = 0
            mid = (min + max) / 2
            for i in range(len(nums)):
                if mid >= nums[i]:
                    cnt += 1
            if cnt > mid:
                max = mid
            else:
                min = mid + 1
        return min

solution = Solution()
nums = [1,1]
print solution.findDuplicate(nums)
