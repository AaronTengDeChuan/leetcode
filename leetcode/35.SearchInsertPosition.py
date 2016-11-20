#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        pre = -1
        while left <= right:
            mid = (left + right) / 2
            pre = mid
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[pre] < target:
            return pre + 1
        else:
            return pre

solution = Solution()
nums = [1,3,5,6]
target = 5.5
print solution.searchInsert(nums,target)

