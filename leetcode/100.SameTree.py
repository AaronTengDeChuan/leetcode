#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right =None

class Solution(object):
    def formerVisited(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                flag1 = self.formerVisited(p.left, q.left)
                flag2 = self.formerVisited(p.right, q.right)
                return flag1 and flag2

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.formerVisited(p, q)

