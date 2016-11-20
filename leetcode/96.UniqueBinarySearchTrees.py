#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = []
        for i in range(n + 1):
            dp.append(0)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]

solution = Solution()
print solution.numTrees(int(raw_input("n = ")))

        
