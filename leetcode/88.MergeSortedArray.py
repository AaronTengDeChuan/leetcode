#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        while m < len(nums1):
            nums1.pop()
        for i in range(n):
            while index < len(nums1) and nums1[index] <= nums2[i]:
                index += 1
            nums1.insert(index, nums2[i])
            index += 1

solution = Solution()
nums1 = [0,1]
nums2 = [1,2]
solution.merge(nums1, 1, nums2, len(nums2))
print nums1
        
