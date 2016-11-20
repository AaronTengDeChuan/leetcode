#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        result.append([1])
        for i in range(1, numRows):
            tmp = []
            tmp.append(1)
            for j in range(1, i):
                tmp.append(result[i - 1][j] + result[i - 1][j - 1])
            tmp.append(1)
            result.append(tmp)
        return result

solution = Solution()
result = solution.generate(int(raw_input("numRows = ")))
for i in result:
    print i

        
