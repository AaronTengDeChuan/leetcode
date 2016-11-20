#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(1, rowIndex + 1):
            for j in range(-1, - len(result), -1):
                result[j] += result[j - 1]
            result.append(1)
        return result

solution = Solution()
print solution.getRow(int(raw_input("rowIndex = ")))
        
