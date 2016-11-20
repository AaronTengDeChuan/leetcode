#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [0]
        max = 0
        for i in wordDict:
            if len(i) > max:
                max = len(i)
        for i in range(len(s)):
            for j in dp[::-1]:
                if (i - j + 1) > max:
                    break
                if s[j:i + 1] in wordDict:
                    dp.append(i + 1)
                    break
        if dp[-1] == len(s):
            return True
        else:
            return False

    def backtracking(self, s, wordDict, min, max):
        if len(s) == 0:
            return True
        elif len(s) < min:
            return False
        else:
            for i in range(min, max + 1):
                if s[:i] not in wordDict:
                    continue
                else:
                    if self.backtracking(s[i:], wordDict, min, max):
                        return True
            return False


    def bt_wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(wordDict) == 0:
            if len(s) != 0:
                return False
            else:
                return True
        min = len(s)
        flag = False 
        max = 0
        for i in wordDict:
            if len(i) <= min:
                flag = True
                min = len(i)
            if len(i) > max:
                max = len(i)
        if flag:
            return self.backtracking(s,wordDict, min, max)
        else:
            return False

solution = Solution()
s = 'leetcode'
wordDict = ("code","leet")
print solution.wordBreak(s, wordDict)

        
