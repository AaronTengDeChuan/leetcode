#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def BST(self, nums, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])
        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        root.left = self.BST(nums, left, mid - 1)
        root.right = self.BST(nums, mid + 1, right)
        return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.BST(nums, 0, len(nums) - 1)
        
