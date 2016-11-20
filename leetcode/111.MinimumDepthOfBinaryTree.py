#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs_depth(self, root):
        if root == None:
            return 0
        else:
            left_depth = self.dfs_depth(root.left)
            right_depth = self.dfs_depth(root.right)
            if left_depth == 0:
                return 1 + right_depth
            elif right_depth == 0:
                return 1 + left_depth
            else:
                return 1 + min(left_depth, right_depth)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #return self.dfs_depth(root)
        if root == None:
            return 0
        min_depth = 1
        num = 1
        queue = [root]
        while len(queue) > 0:
            tmp = queue[0]
            del queue[0]
            num -= 1
            if tmp.right == None and tmp.left == None:
                break
            else:
                if tmp.left != None:
                    queue.append(tmp.left)
                if tmp.right != None:
                    queue.append(tmp.right)
            if num == 0:
                min_depth += 1
                num = len(queue)
        return min_depth


