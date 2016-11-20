#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        greater = ListNode(0)
        tmp = ListNode(0)
        tmp.next = head
        p = head
        pre = tmp
        q = greater
        while p != None:
            if p.val >= x:
                q.next = p
                pre.next = p.next
                p = p.next
                q = q.next 
                q.next = None
            else:
                p = p.next
                pre = pre.next
        p = tmp
        while p.next != None:
            p = p.next
        p.next = greater.next
        return tmp.next
        
