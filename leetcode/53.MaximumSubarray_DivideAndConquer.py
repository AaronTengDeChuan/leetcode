#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def divideAndConquer(self, nums, begin, end):
        if begin == end:
            return nums[begin]
        mid = (begin + end) / 2
        leftMax = self.divideAndConquer(nums, begin,mid)
        rightMax = self.divideAndConquer(nums, mid + 1, end)
        leftMid = nums[mid]
        midRight = nums[mid + 1]
        sum = leftMid
        for i in range(mid - 1, begin - 1, -1):
            sum += nums[i]
            if sum > leftMid:
                leftMid = sum
        sum = midRight
        for i in range(mid + 2, end + 1):
            sum += nums[i]
            if sum > midRight:
                midRight = sum
        return max(leftMid + midRight, max(leftMax, rightMax))


    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.divideAndConquer(nums, 0, len(nums) - 1)
        

solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print solution.maxSubArray(nums)

