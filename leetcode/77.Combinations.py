#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def backtracking(self, results, nums , i, n, k, value_list):
        if k == 0:
            results.append([i for i in value_list])
            return 
        for j in range(i, n - k + 1):
            self.backtracking(results, nums, j + 1, n, k - 1, value_list + [nums[j]])


    def combine(self, n, k):
        nums = []
        results = []
        if n == 0 or k == 0:
            return results
        for i in range(1, n + 1):
            nums.append(i)
        self.backtracking(results, nums, 0, n, k, [])
        return results
solution = Solution()
n = 4
k = 2
results = solution.combine(n, k)
for i in results:
    print i

