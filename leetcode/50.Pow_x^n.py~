#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = False
        if n < 0:
            flag = True
            n = -n
        result = 1.0
        curPow = x
        while n != 0:
            if n % 2 == 1:
                result *= curPow
            curPow *=curPow
            n = n / 2
        if flag:
            result = 1 / result
        return result

solution = Solution()
x = raw_input("x = ")
n = raw_input("n = ")
print solution.myPow(float(x), int(n))
