#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def search(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[right]:
                #第一种情况
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] <= nums[mid]:
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1 
        return -1

nums = [3,1]
solution = Solution()
target = int(raw_input("Enter your input:"))
print "The result is " , solution.search(nums,target)


