#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def nowswap(self, nums, start, end):
        if start == end:
            return True
        for i in range(start, end):
            if nums[end] == nums[i]:
                return False
        return True

    def dfs(self, i, nums, results):
        if i == len(nums):
            results.append([j for j in nums])
            return
        for j in range(i, len(nums)):
            if not self.nowswap(nums, i, j):
                continue
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(i + 1, nums, results)
            nums[i], nums[j] = nums[j], nums[i]

    def permuteUnique(self, nums):
        results = []
        self.dfs(0, nums, results)
        return results

solution = Solution()
nums = [1,1,2,2]
print solution.permuteUnique(nums)

