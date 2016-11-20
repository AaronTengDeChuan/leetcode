#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pre = root
        cur = None
        while pre != None:
            while pre != None and pre.left == None and pre.right == None:
                pre = pre.next
            if pre == None:
                break
            if pre.left != None:
                cur = pre.left
            else:
                cur = pre.right
            tmp = TreeLinkNode(0)
            while pre != None:
                if pre.left != None:
                    tmp.next = pre.left
                    tmp = tmp.next
                if pre.right != None:
                    tmp.next = pre.right
                    tmp = tmp.next
                pre = pre.next
            pre = cur
