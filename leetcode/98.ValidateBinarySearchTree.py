#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cur_max = None
        pre = None
        while root != None:
            if root.left == None:
                if cur_max != None and cur_max.val >= root.val:
                    return False
                cur_max = root
                root = root.right
            else:
                pre = root.left
                while pre.right != None and pre.right != root:
                    pre = pre.right
                if pre.right == None:
                    pre.right = root
                    root = root.left
                else:
                    if cur_max.val >= root.val:
                        return False
                    cur_max = root
                    pre.right = None
                    root = root.right
        return True

        
