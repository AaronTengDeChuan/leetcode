#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        queue = [root]
        while len(queue) > 0:
            tmp = [j for j in queue]
            queue = []
            res = []
            for i in tmp:
                res.append(i.val)
                if i.left != None:
                    queue.append(i.left)
                if i.right != None:
                    queue.append(i.right)
            result.append([i for i in res ])
        return result


        
