#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        results = []
        candidates.sort(key = lambda number : number)
        self.solveSum(candidates, target, 0, results, result)
        return results

    def solveSum(self, candidate, target, index, results, result):
        if target == 0:
            if result not in results:
                results.append([i for i in result])
            return
        if index >= len(candidate) or candidate[index] > target:
            return
        for i in range(index, len(candidate)):
            if candidate[i] > target:
                break
            result.append(candidate[i])
            self.solveSum(candidate, target - candidate[i], i + 1, results, result)
            result.pop()


solution = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print solution.combinationSum2(candidates , target)
