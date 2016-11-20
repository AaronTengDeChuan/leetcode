#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        sum = len(s3)
        if sum != m + n:
            return False
        dp = []
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                tmp.append(False)
            dp.append([item for item in tmp])
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                index = i + j - 1
                if index < 0:
                    continue
                else:
                    if i > 0 and s1[i - 1] == s3[index] and dp[i - 1][j] == True:
                        dp[i][j] = True
                    elif j > 0 and s2[j - 1] == s3[index] and dp[i][j - 1] == True:
                        dp[i][j] = True
        return dp[m][n]

solution = Solution()
print solution.isInterleave(raw_input("s1 = "), raw_input("s2 = "), raw_input("s3 = "))      


        
