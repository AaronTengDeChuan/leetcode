#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def dfs(self, i, nums, results):
        if i == len(nums):
            results.append([j for j in nums])
            return
        for j in range(i,len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(i + 1, nums, results)
            nums[i], nums[j] = nums[j], nums[i]

    def permute(self, nums):
        results = []
        self.dfs(0, nums, results)
        return results

solution = Solution()
nums = [1,2,3,4]
print solution.permute(nums)

