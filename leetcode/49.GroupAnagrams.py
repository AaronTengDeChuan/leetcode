#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def str_sort(self, s):
        str_list = list(s)
        str_list.sort()
        s = "".join(str_list)
        return s

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        results = {}
        ans = []
        for i in strs:
            tmp = self.str_sort(i)
            if tmp in results:
                results[tmp].append(i)
            else:
                results[tmp] = [i]
        for i in results:
            ans.append(results[i])
        return ans

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
results = solution.groupAnagrams(strs)
for i in range(len(results)):
    print results[i]


