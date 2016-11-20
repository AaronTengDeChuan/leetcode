#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        results = []
        candidates.sort(key = lambda number : number)
        candidate = []
        [ candidate.append(i) for i in candidates if not i in candidate]
        self.solveSum(candidate, target, 0, results, result)
        return results

    def solveSum(self, candidate, target, index, results, result):
        if target == 0:
            results.append([i for i in result])
            return
        if index >= len(candidate) or candidate[index] > target:
            return
        for i in range(index, len(candidate)):
            result.append(candidate[i])
            self.solveSum(candidate, target - candidate[i], i, results, result)
            result.pop()


solution = Solution()
candidates = []
target = 4
print solution.combinationSum(candidates , target)
