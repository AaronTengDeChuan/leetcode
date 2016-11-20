#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def backtracking(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None or root1.val != root2.val:
            return False
        else:
            if self.backtracking(root1.left, root2.right) and self.backtracking(root1.right, root2.left):
                return True
            else:
                return False
    def isSymmetric(self, root):
        """
        non-recursive preorder
        """
        if root == None:
            return True
        stack1 = [root.left]
        stack2 = [root.right]
        cur1 = root.left
        cur2 = root.right
        if cur1 == None and cur2 == None:
            return True
        while len(stack1) >= 1 and len(stack2) >= 1:
            if cur1 == None and cur2 == None:
                cur1 = stack1.pop()
                cur2 = stack2.pop()
                cur1 = cur1.right
                cur2 = cur2.left
            elif cur1 == None or cur2 == None or cur1.val != cur2.val:
                return False
            else:
                stack1.append(cur1)
                stack2.append(cur2)
                cur1 = cur1.left
                cur2 = cur2.right
        return True

    def isSymmetric_recurse(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.backtracking(root.left, root.right)
        
