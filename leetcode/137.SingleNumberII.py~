#!usr/bin/env python
#!encoding:utf-8
import sys

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        tmp = 1
        for i in xrange(32):
            count = 0
            for j in nums:
                if j&tmp != 0:
                    count += 1
            count %= 3
            if count == 1 and i != 31:
                res |= tmp
            elif i == 31 and count == 1:
                res = -(2 ** 31 - res)
            tmp <<= 1
        return res

solution = Solution()
nums = [1,2,3,1,2,3,-4,1,2,3]
print solution.singleNumber(nums)
                

        
