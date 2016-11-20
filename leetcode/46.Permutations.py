#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def backtracking(self, results, result, nums):
        if len(nums) == 0:
            results.append([i for i in result])
            return
        num = [i for i in nums]
        for i in num:
            result.append(i)
            nums.remove(i)
            self.backtracking(results, result, nums)
            result.remove(i)
            nums = [i for i in num]


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        result = []
        self.backtracking(results, result, nums)
        return results

solution = Solution()
nums = [1,2,3,4]
print solution.permute(nums)

