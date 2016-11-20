#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        while root != None:
            if root.left != None:
                pre = root.left
                while pre.right != None:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
    def flatten_origin(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        end = None
        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                end = cur
                cur = cur.left
            tmp = stack.pop()
            end.right = tmp.right
            if tmp.left != None:
                tmp.right = tmp.left
                tmp.left = None
            cur = end.right
        
