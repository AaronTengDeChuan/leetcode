#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum_recurse(self, root, sum, result, value_list):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """ 
        if root == None:
            return
        elif root.left == None and root.right == None and root.val == sum:
            result.append([i for i in value_list] + [root.val])
            return
        else:
             self.hasPathSum_recurse(root.left, sum - root.val, result, value_list + [root.val])
             self.hasPathSum_recurse(root.right, sum - root.val, result, value_list + [root.val])

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.hasPathSum_recurse(root, sum, result, [])
        return result
    
