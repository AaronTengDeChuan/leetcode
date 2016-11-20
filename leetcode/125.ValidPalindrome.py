#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def isAlphanumeric(self, c):
        if ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
            return True
        else:
            return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not self.isAlphanumeric(s[i]):
                i += 1
            while i < j and not self.isAlphanumeric(s[j]):
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True

solution = Solution()
print solution.isPalindrome(raw_input("s = "))
