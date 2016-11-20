#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs_depth(self, depth, root):
        if root == None:
            return depth
        else:
            left_depth = self.dfs_depth(depth + 1, root.left)
            right_depth = self.dfs_depth(depth + 1, root.right)
            return max(left_depth, right_depth)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        return self.dfs_depth(depth, root)
        
