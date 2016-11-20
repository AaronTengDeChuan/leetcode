#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        last = 0
        for i in range(-1, - len(s) - 1, -1):
            if s[i] == ' ':
                break
            else:
                last += 1
        return last
solution = Solution()
s = "  a  "
print solution.lengthOfLastWord(s)
