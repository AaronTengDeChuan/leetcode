#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        for i in range(len(nums)):
            tmp = []
            for j in results:
                tmp.append(j + [nums[i]])
            results += tmp
        return results

solution = Solution()
nums = [1,2,3]
results = solution.subsets(nums)
for i in results:
    print i
