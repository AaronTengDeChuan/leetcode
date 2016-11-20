#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs_buildTree(self, inorder, postorder, in_start, post_start, len):
        if len == 0:
            return None
        for i in range(in_start, in_start + len):
            if postorder[post_start + len - 1] == inorder[i]:
                break
        root = TreeNode(postorder[post_start + len - 1])
        root.left = self.dfs_buildTree(inorder, postorder,in_start, post_start, i - in_start)
        root.right = self.dfs_buildTree(inorder, postorder, i + 1, post_start + i - in_start, len - i + in_start - 1)
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs_buildTree(inorder, postorder, 0, 0, len(inorder))
        
