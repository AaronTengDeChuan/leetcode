#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == nums[mid]:
                return True
            if nums[mid] > nums[left]:
                if target < nums[mid] and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < num[left]:
                if target > nums[mid] and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False

