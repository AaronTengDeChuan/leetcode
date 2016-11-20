#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        result = []
        if root == None:
            return result
        stack = [root]
        head = root
        while stack:
            cur = stack[-1]
            if cur.left == head or cur.right == head or cur.left == None and cur.right == None:
                stack.pop()
                result.append(cur.val)
                head = cur
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return result

    def postorderTraversal_First(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        while root or stack:
            while root:
                stack.append((root, False))
                root = root.left
            temp = stack.pop()
            if temp[1]:
                result.append(temp[0].val)
            else:
                root = temp[0].right
                stack.append((temp[0], True))
        return result

solution = Solution()
root = TreeNode(1)
p = root
p.right = TreeNode(2)
p = p.right
p.left = TreeNode(3)
print solution.postorderTraversal(root)

