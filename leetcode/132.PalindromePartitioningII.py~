#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s) for i in range(len(s))]
        count = [len(s)] * (len(s) + 1)
        count[len(s)] = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if j == len(s) - 1:
                        count[i] = 0
                    elif count[i] > 1 + count[j + 1]:
                        count[i] = 1 + count[j + 1]
        return count[0]

solution = Solution()
result = solution.minCut(raw_input("s = "))
print result
