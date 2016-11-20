#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        set = []
        p = head
        while p != None:
            set.append(p)
            p = p.next
        i = 0
        j = len(set) - 1
        while i < j:
            set[i].next = set[j]
            if j - i == 1:
                set[j].next = None
            else:
                set[j].next = set[i + 1]
                if j - i == 2:
                    set[i + 1].next = None
            i += 1
            j -= 1
