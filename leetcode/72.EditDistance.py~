#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        dp = []
        for i in range(len1 + 1):
            tmp = []
            for j in range(len2 + 1):
                tmp.append(0)
            dp.append(tmp)
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(1,len1 + 1):
            for j in range(1,len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        return dp[i][j]


word1 = raw_input("s = ")
word2 = raw_input("p = ")
solution = Solution()
print solution.minDistance(word1,word2)

