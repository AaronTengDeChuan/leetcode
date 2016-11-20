#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def convert(self ,s):
        sum = 0
        index = 0
        while index < len(s) and s[index] == '0':
            index += 1
        for i in s[index:]:
            sum *= 10
            sum += ord(i) - ord('0')
        return sum

    def backtracking(self, result, s, i ,num , value):
        if num == 0:
            if i >= len(s):
                result.append(value[1:])
            return
        elif i >= len(s):
            return
        elif s[i] != '0':
            for j in range(i, min(i + 3,len(s))):
                if self.convert(s[i:j + 1]) <= 255:
                    self.backtracking(result, s, j + 1, num - 1, value + "."+ s[i:j + 1])
        else:
            self.backtracking(result, s, i + 1, num - 1, value + "." + s[i])



    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.backtracking(result, s, 0, 4, "")
        return result

solution = Solution()
s = "010010"
for i in solution.restoreIpAddresses(s):
    print i
        
        
