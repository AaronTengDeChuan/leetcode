#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = [[]]
        start = 0
        for i in range(len(nums)):
            j = 0
            if i > 0 and nums[i] == nums[i - 1]:
                j = start
                start = len(results)
            else:
                start = len(results)
            tmp = []
            for k in range(j, len(results)):
                tmp.append(results[k] + [nums[i]])
            results += tmp
        return results

solution = Solution()
nums = [1,2,3,3,3]
results = solution.subsetsWithDup(nums)
for i in results:
    print i
