#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        while root or stack:
            while root != None:
                result.append(root.val)
                stack.append(root)
                root = root.left
            temp = stack.pop()
            root = temp.right
        return result

solution = Solution()

print solution.preorderTraversal(root)


