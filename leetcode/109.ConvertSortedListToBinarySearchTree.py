#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def bottom_to_up_BST(self, head, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        left_tree = self.bottom_to_up_BST(head, left, mid - 1)
        root = TreeNode(head[0].val)
        root.left = left_tree
        head[0] = head[0].next
        root.right = self.bottom_to_up_BST(head, mid + 1,right)
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p = head
        length = 0
        while p != None:
            length += 1
            p = p.next
        return self.bottom_to_up_BST([head], 0, length - 1)

