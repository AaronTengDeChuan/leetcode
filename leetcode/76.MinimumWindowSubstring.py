#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) == 0:
            return ""
        left = -1
        right = -1
        min = len(s) + 1
        min_left = 0
        min_right = 0
        dict = {}
        for i in t:
            dict[i] = -1
        unic = len(dict)
        for i in range(len(s)):
            if s[i] in dict:
                right = i
                if dict[s[i]] == -1:
                    if left == -1:
                        left = i
                    unic -= 1
                    dict[s[i]] = i
                    if unic == 0:
                        min = right - left + 1
                        min_left = left
                        min_right = right
                else:
                    if dict[s[i]] == left:
                        dict[s[i]] = i
                        tmp = i
                        for j in dict.values():
                            if j >= 0 and tmp > j:
                                tmp = j
                        left = tmp
                        if unic == 0:
                            if(right - left + 1) < min:
                                min = right - left + 1
                                min_left = left
                                min_right = right
                    else:
                        dict[s[i]]= i
        if min > len(s) or min < len(t):
            return ""
        else:
            return s[min_left:min_right + 1]

solution = Solution()
s = "ADOBECOEBAN"
t = "ABC"
print solution.minWindow(s, t)


