#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = []
        for i in range(len(s) + 1):
            tmp = []
            for j in range(len(p) + 1):
                tmp.append(False)
            dp.append(tmp)
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] != '*':
                    dp[i][j] = False
                else:
                    for k in range(i + 1):
                        if dp[k][j - 1] == True:
                            dp[i][j] = True
                            break
        return dp[len(s)][len(p)]


solution = Solution()
#s = raw_input("s = ")
#p = raw_input("p = ")
s = "aabbabbaabbbbaabaabaaabaaaabbabaabbaaaaaababaaaaaaaaabaaaaababbbaabbbabbbbabbbbbbabbbbbbabbababbbbaabababbabababbaabbaabbbaaababaabbaaaabababbbbbaabaaabaaaaaabaaaabaabbaabbbbabbaabbaabbabbaabbabaabbbb"
p = "bbb***bba*ab**a*b***b*a**a*****a***b*a**a***b*b***b****b*ba*a***bbb******ba*bbb*a***aba**ab*****b****ab"
print solution.isMatch(s, p)
