#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return sys.maxint
        flag = 0
        if dividend < 0:
            flag += 1
            dividend = -dividend
        if divisor < 0:
            flag += 1
            divisor = -divisor
        sum = divisor
        num = 1
        result = 0
        while sum <= dividend:
            num += num
            sum += sum
        num >>= 1
        sum >>= 1
        while dividend >= divisor:
            if dividend >= sum:
                result += num
                dividend -= sum
            sum >>= 1
            num >>= 1
        if flag == 1:
            return -result
        else:
            if result > 2147483647:
                return 2147483647
            return result


solution = Solution()
dividend = raw_input("dividend = ")
divisor = raw_input("divisor = ")
print solution.divide(int(dividend), int(divisor))
