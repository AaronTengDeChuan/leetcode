#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def recurse(self, head):
        if head.next == None:
            return head, head
        first, last = self.recurse(head.next)
        head.next = last.next
        last.next = head
        return first,last

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        first, last = self.reverseList(head)
        return first


    def reverseList_iterate(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        tmp = ListNode(0)
        p = head
        while p != None:
            pre = p.next
            p.next = tmp.next
            tmp.next = p
            p = pre
        return tmp.next
        
        
