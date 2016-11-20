#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        stack = [root]
        flag = True
        while len(stack) > 0:
            tmp = [j for j in stack]
            stack = []
            res = []
            while len(tmp) > 0:
                i = tmp.pop()
                res.append(i.val)
                if flag == True:
                    if i.left != None:
                        stack.append(i.left)
                    if i.right != None:
                        stack.append(i.right)
                else:
                    if i.right != None:
                        stack.append(i.right)
                    if i.left != None:
                        stack.append(i.left)
            result.append([i for i in res ])
            flag = -flag
        return result
        
