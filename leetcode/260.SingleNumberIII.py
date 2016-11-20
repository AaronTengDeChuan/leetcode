#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        one_pass = 0
        for i in nums:
            one_pass ^= i
        temp = 1
        while temp&one_pass == 0:
            temp <<= 1
        group_one = 0
        group_two = 0
        for i in nums:
            if i&temp == 0:
                group_one ^= i
            else:
                group_two ^= i
        return [group_one, group_two]

nums = [1,-2,1,-3,-2,5]
solution = Solution()
print solution.singleNumber(nums)
