#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        convert = [
            [-1, 0, 3, 2,-1, 1],
            [-1, 8,-1, 4, 5, 1],
            [-1,-1,-1,-1,-1, 4],
            [-1,-1,-1, 2,-1, 1],
            [-1, 8,-1,-1, 5, 4],
            [-1,-1, 6,-1,-1, 7],
            [-1,-1,-1,-1,-1, 7],
            [-1, 8,-1,-1,-1, 7],
            [-1, 8,-1,-1,-1,-1]
        ]
        """
        input type:
        0:invalid character
        1:space
        2:sign
        3:point
        4:e
        5:digit
        """
        state = 0
        for i in range(len(s)):
            input = 0
            if s[i] == ' ':
                input = 1
            elif s[i] == '+' or s[i] == '-':
                input = 2
            elif s[i] == '.':
                input = 3
            elif s[i] == 'e' or s[i] == 'E':
                input = 4
            elif s[i] >= '0' and s[i] <= '9':
                input = 5
            else:
                input = 0
            state = convert[state][input]
            if state == -1:
                return False
        if state in [1,4,7,8]:
            return True
        else:
            return False

solution = Solution()
s = raw_input("s = ")
print solution.isNumber(s)


