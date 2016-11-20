#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        if len(s) == 0 or s[0] == '0':
            return 0
        pre_one = 1
        pre_two = 1
        for i in range(1,len(s)):
            if s[i] == '0':
                if 0 < ord(s[i - 1]) - ord('0') <= 2:
                    pre_one = pre_two
                else:
                    return 0
            elif 10 <= (ord(s[i]) - ord('0') + (ord(s[i - 1]) - ord('0'))* 10)<= 26:
                tmp = pre_one
                pre_one += pre_two
                pre_two = tmp
            else:
                pre_two = pre_one
        return pre_one

solution = Solution()
s = "227"
print solution.numDecodings(s)
            
        
