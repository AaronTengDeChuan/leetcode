#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getHeight(self, root):
        if root == None:
            return 0
        left = self.getHeight(root.left)
        if left == -1:
            return -1
        right = self.getHeight(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)

    def height_balanced(self, root, flag):
        if root == None:
            return 0
        left = self.height_balanced(root.left, flag)
        right = self.height_balanced(root.right, flag)
        if abs(left - right) > 1:
            flag[0] = False
        return 1 + max(left, right)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #flag = [True]
        #self.height_balanced(root, flag)
        if self.getHeight(root) == -1:
            return False
        else:
            return True

        
