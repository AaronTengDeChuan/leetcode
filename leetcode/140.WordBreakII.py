#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dp = [[0]]
        max = 0
        for i in wordDict:
            if len(i) > max:
                max = len(i)
        for i in range(len(s)):
            flag = True
            for j in dp[::-1]:
                if (i - j[0] + 1) > max:
                    break
                if s[j[0]:i + 1] in wordDict:
                    if flag:
                        dp.append([i + 1])
                        flag = False
                    dp[-1].append(j[0])
        if dp[-1][0] != len(s):
            return []
        result = []
        for i in dp:
            print i 
        self.convert(s, dp, len(s), result, "")
        return result

    def convert(self, s, dp, end, result, value_str):
        if end == 0:
            result.append(value_str)
            return 
        for i in dp:
            if i[0] == end:
                for j in i[1:]:
                    temp = ""
                    if len(value_str) == 0:
                        temp = s[j:end]
                    else:
                        temp = s[j:end] + ' '
                    self.convert(s, dp, j, result, temp + value_str)

                    
            
        
    
    def backtracking(self, s, i, wordDict, dp, max, result, value_str):
        if len(s) == 0:
            result.append(value_str[:])
            return 
        elif len(s) < min:
            return
        else:
            for j in range(i,i+max):
                for k in dp[::-1]:
                    if (j - k + 1) > max:
                        break
                    if s[k : j + 1] in wordDict:
                        self.backtracking()
            for j in dp[::-1]:
                if(i - j + 1) > max:
                    break
                if s[j:i + 1] in wordDict:
                    dp.append(i + 1)
                    
solution = Solution()
s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
for i in solution.wordBreak(s, dict):
    print i
