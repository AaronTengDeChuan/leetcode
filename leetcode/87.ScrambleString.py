#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def backtracking(self, s1, s2):
        if s1 == s2:
            return True
        elif len(s1) == 1:
            return False
        else:
            for i in range(1,len(s1)):
                if self.backtracking(s1[:i], s2[len(s1) - i:]) and self.backtracking(s1[i:], s2[:len(s1) - i]) or self.backtracking(s1[:i], s2[:i]) and self.backtracking(s1[i:], s2[i:]):
                    return True
            return False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.backtracking(s1, s2)

solution = Solution()
print solution.isScramble(raw_input("s1 = "), raw_input("s2 = "))
        
        
