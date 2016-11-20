#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        p = RandomListNode(head.label)
        dict = {head:p}
        result = p
        while head != None:
            if head.next != None:
                if head.next in dict:
                    result.next = dict[head.next]
                else:
                    result.next = RandomListNode(head.next.label)
                    dict[head.next] = result.next
            if head.random != None:
                if head.random in dict:
                    result.random = dict[head.random]
                else:
                    result.random = RandomListNode(head.random.label)
                    dict[head.random] = result.random
            head = head.next
            result = result.next
        return p

solution = Solution()
head = RandomListNode(1)
head.next = None
head.random = head
head = solution.copyRandomList(head)
while head != None:
    print head.label,'(' + str(head.random.label) + ')',
    head = head.next




