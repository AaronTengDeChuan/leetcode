#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        single_speed = head
        double_speed = head
        while single_speed != None:
            single_speed = single_speed.next
            if double_speed.next != None and double_speed.next.next != None:
                double_speed = double_speed.next.next
            else:
                return False
            if single_speed == double_speed:
                return True
        return False
        
