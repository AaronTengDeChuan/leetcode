#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        if n <= 0:
            return result
        sum = 1
        for i in range(n):
            tmp = []
            for i in result[::-1]:
                tmp.append(i + sum)
            result.extend([j for j in tmp])
            sum *= 2
        return result
solution = Solution()
n = 3
print solution.grayCode(n)
        
