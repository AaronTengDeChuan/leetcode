#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def backtracking(self, s, start, result, value_list):
        if start == len(s):
            result.append([w for w in value_list])
        for i in range(1, len(s) - start + 1):
            if self.isPalindrome(s[start:start + i]):
                self.backtracking(s, start + i, result, value_list + [s[start:start + i]])
            
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if len(s) == 0:
            return result
        self.backtracking(s, 0, result, [])
        return result

solution = Solution()
result = solution.partition(raw_input("s = "))
for i in result:
    print i
        
