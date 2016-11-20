#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def convertToSay(self, say):
        s = ""
        count = 1
        current = say[0]
        i = 1
        while i < len(say) + 1:
            if i < len(say) and say[i] == current:
                count += 1
                i += 1
            else:
                s += str(count)
                s += current
                count = 1
                if i < len(say):
                    current = say[i]
                i += 1
        return s


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        for i in range(1,n):
            say = self.convertToSay(say)
        return say

solution = Solution()
n = 12
print solution.countAndSay(n)
