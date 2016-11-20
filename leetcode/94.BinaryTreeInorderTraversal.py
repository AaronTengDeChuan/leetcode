#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        cur = root
        pre = None
        while cur != None:
            if cur.left == None:
                result.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right != None and pre.right != cur:
                    pre = pre.right
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else:
                    result.append(cur.val)
                    cur= cur.right
        return result

    def inorderTraversal_n_space(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        p = root
        stack = []
        while len(stack) > 0 or p != None:
            while p != None:
                stack.append(p)
                p = p.left
            p = stack.pop()
            result.append(p.val)
            p = p.right
        return result

solution = Solution()
root = TreeNode(1)
p = root 
p.left = None
p.right = TreeNode(2)
p = p.right 
p.left = TreeNode(3)
print solution.inorderTraversal(root)
            
        
