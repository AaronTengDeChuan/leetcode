#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def longestValidParentheses(self,s):
        """
        :type s: str
        :rtype: int
        """
        dp_list = []
        max_len = 0
        for i in range(len(s)):
            dp_list.append(0)
        for j in range(-2,-len(s) - 1,-1):
            end = j + dp_list[j+1] + 1
            if s[j] == '(':
                if end < 0 and s[end] == ')':
                    dp_list[j] = dp_list[j+1] + 2
                    if end + 1 < 0:
                        dp_list[j] += dp_list[end+1]
            if max_len < dp_list[j]:
                max_len = dp_list[j]
        return max_len

s = "()"
solution = Solution()
print solution.longestValidParentheses(s)

