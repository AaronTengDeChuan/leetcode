#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        len = n - m
        first = head
        p = head
        for i in range(m - 1):
            first = p 
            p = p.next
        pre = p
        p = p.next
        end = pre
        for i in range(len):
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        end.next = p
        if m == 1:
            return pre
        else:
            first.next = pre
            return head



        
