#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int 
        """
        if len(nums) < 2:
            return len(nums)
        count = 0
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count +=1
                if count >= 2:
                    continue
            else:
                count = 0
            nums[cur] = nums[i]
            cur += 1
        return cur

solution = Solution()
nums = [1,1,1,2,2,3]
print solution.removeDuplicates(nums)
print nums

