#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type l: int
        :rtype: str
        """
        sum = 1
        result = ""
        for i in range(1, n):
            sum *= i
        set = []
        for i in range(n):
            set.append(i + 1)
        k -= 1
        for i in range(n):
            order = k / sum
            k %= sum
            result += chr(set[order] + ord('0'))
            del set[order]
            if i != n - 1:
                sum /= (n - i - 1)
        return result

solution = Solution()
n = 4
sum = 1
for i in range(1,n + 1):
    sum *= i
for k in range(1,sum + 1):
    print solution.getPermutation(n, k)

