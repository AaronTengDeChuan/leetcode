#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs_buildTree(self, preorder, inorder, pre_start, in_start, len):
        if len == 0:
            return None
        for i in range(in_start, in_start + len):
            if preorder[pre_start] == inorder[i]:
                break
        root = TreeNode(preorder[pre_start])
        root.left = self.dfs_buildTree(preorder, inorder, pre_start + 1, in_start, i - in_start)
        root.right = self.dfs_buildTree(preorder, inorder, pre_start + i - in_start + 1, i + 1, len - i + in_start - 1)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs_buildTree(preorder, inorder, 0, 0, len(preorder))
        
