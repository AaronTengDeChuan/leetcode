#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        result = [-1,-1]
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if right == mid:
                    break
                right = mid
        if nums[left] == target:
            result[0] = left
        elif nums[right] == target:
            result[0] = right
        else:
            return result
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if left == mid:
                    break
                left = mid
        if nums[right] == target:
            result[1] = right
        elif nums[left] == target:
            result[1] = left
        else:
            return result
        return result


solution = Solution()
nums = [2,2]
target = 2
print solution.searchRange(nums,target)
