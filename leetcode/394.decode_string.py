#!usr/bin/env python
import sys

class Solution(object):
    def isWhat(self, character):
        if ord('0') <= ord(character) <= ord('9'):
            return 0
        if ord('a') <= ord(character) <= ord('z') or ord('A') <= ord(character) <= ord('Z'):
            return 1
        return -1

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        index = 0
        strlen = len(s)
        counts = 0
        while index < strlen:
            if self.isWhat(s[index]) == 1:
                result += s[index]
                index += 1
            elif self.isWhat(s[index]) == 0:
                counts *= 10
                counts += ord(s[index]) - ord('0')
                index += 1
            elif s[index] == '[':
                left_brackets = 1
                start = index + 1
                while left_brackets:
                    if s[start] == '[':
                        left_brackets += 1
                    elif s[start] == ']':
                        left_brackets -= 1
                    start += 1
                result += self.decodeString(s[index + 1: start - 1]) * counts
                counts = 0
                index = start
        return result

solution = Solution()
s = raw_input("s = ")
print solution.decodeString(s)