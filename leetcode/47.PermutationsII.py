#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def dfs(self, i, nums, results):
        if i == len(nums):
            if nums not in results:
                results.append([j for j in nums])
            return
        for j in range(i,len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(i + 1, nums, results)
            nums[i], nums[j] = nums[j], nums[i]

    def permuteUnique(self, nums):
        results = []
        self.dfs(0, nums, results)
        return results

solution = Solution()
nums = [1,1,2]
print solution.permuteUnique(nums)

