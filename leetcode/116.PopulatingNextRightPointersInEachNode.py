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
        if root == None:
            return
        pre = root
        cur = None
        while pre.left != None and pre.right != None:
            cur = pre.left
            tmp = TreeLinkNode(0)
            while pre != None:
                tmp.next = pre.left
                pre.left.next = pre.right
                tmp = pre.right
                pre = pre.next
            pre = cur

    def dfs_log_n_space(self, root):
        if root == None or root.left == None and root.right == None:
            return
        l = root.left
        r = root.right
        while l != None:
            l.next = r
            l = l.right
            r = r.left
        self.dfs(root.left)
        self.dfs(root.right)

    def connect_n_space(self, root):
        if root == None:
            return
        queue = [root]
        while len(queue) > 0:
            tmp = [i for i in queue]
            queue = []
            for i in range(len(tmp)):
                if tmp[i].left != None:
                    queue.append(tmp[i].left)
                if tmp[i].right != None:
                    queue.append(tmp[i].right)
                if i == len(tmp) - 1:
                    tmp[i].next = None
                else:
                    tmp[i].next = tmp[i + 1]

