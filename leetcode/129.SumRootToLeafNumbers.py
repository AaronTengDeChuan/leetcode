#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def DFS(self, root, result, value_list):
        if root == None:
            return
        elif root.right == None and root.left == None:
            result.append(value_list + [root.val])
            return
        else:
            self.DFS(root.left, result, value_list + [root.val])
            self.DFS(root.right, result, value_list + [root.val])
    
    def toNumeric(self, nums):
        sum = 0
        for i in nums:
            sum *= 10
            sum += i
        return sum

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        self.DFS(root, result, [])
        sum = 0
        for i in [self.toNumeric(w) for w in result]:
            sum += i
        return sum

        
