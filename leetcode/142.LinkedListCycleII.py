#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
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
                return None
            if single_speed == double_speed:
                start = head
                while start != single_speed:
                    start = start.next
                    single_speed = single_speed.next
                return start
        return None
        
