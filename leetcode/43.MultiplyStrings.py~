#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def add(self, num1, num2):
        result = ""
        carry = 0
        for i in range(min(len(num1), len(num2))):
            sum = (ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0')) + carry
            carry = sum / 10
            c = sum % 10 + ord('0')
            result += chr(c)
        if len(num1) == 0 or len(num2) == 0:
            i = -1
        if len(num1) < len(num2):
            for j in range(i + 1, len(num2)):
                sum = ord(num2[j]) - ord('0') + carry
                carry = sum / 10
                c = sum % 10 + ord('0')
                result += chr(c)
        if len(num1) > len(num2):
            for j in range(i + 1,len(num1)):
                sum = ord(num1[j]) - ord('0') +carry
                carry = sum / 10
                c = sum % 10 + ord('0')
                result += chr(c)
        c = carry + ord('0')
        result += chr(c)
        return result


    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ""
        for i in range(-1, -len(num1) - 1, -1):
            temp = ""
            carry = 0
            for j in range(-1, -len(num2) - 1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + carry
                carry = mul / 10
                c = mul % 10 + ord('0')
                temp += chr(c)
            c = carry + ord('0')
            temp += chr(c)
            result = self.add(result, temp)
            num2 += '0'
        res = ""
        i = -1
        while i > -len(result) and result[i] == '0':
            i -= 1
        for j in range(i, - len(result) - 1, -1):
                res += result[j]
        return res

solution = Solution()
num1 = "0"
num2 = "0"
print solution.multiply(num1, num2)
