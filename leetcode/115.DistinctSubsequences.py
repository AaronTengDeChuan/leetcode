#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        if m == 0:
            return 1
        if n < m:
            return 0
        dp = []
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                tmp.append(0)
            dp.append(tmp)
        for i in range(n + 1):
            dp[0][i] = 1
        for i in range(1, m + 1):
            for j in range(i, n + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                    dp[i][j] += dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[m][n]

solution = Solution()
print solution.numDistinct(raw_input("s = "), raw_input("t = "))
        
