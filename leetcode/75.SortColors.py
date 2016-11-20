#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything. modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                i += 1
                continue
            elif nums[i] == 0:
                if i >= left:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
			#交换过来的元素也要进行判断，所以这里不做 遍历指针后移一位 的操作
                    continue
                i += 1
            else:
                if i <= right:
                    nums[i], nums[right] = nums[right], nums[i]
			#交换过来的元素也要进行判断，所以这里不做 遍历指针后移一位 的操作
                    right -= 1
                    continue
                i += 1

solution = Solution()
nums = [1,2,0]
solution.sortColors(nums)
print nums
