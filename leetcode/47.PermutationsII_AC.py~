#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def backtracking(self, results, result, nums):
        if len(nums) == 0:
            results.append([i for i in result])
            return
        num = []
        [num.append(i) for i in nums if i not in num]
        num_rev = [i for i in nums]
        for i in num:
            result.append(i)
            nums.remove(i)
            self.backtracking(results, result, nums)
            result.pop()
            nums = [j for j in num_rev]


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        result = []
        self.backtracking(results, result, nums)
        return results

solution = Solution()
nums = [1,1,2,2]
print solution.permuteUnique(nums)

