#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
#两个指针，一个指向左边链表的最右端，另一个指向右边链表的最右端
        p = head
        len = 0
        while p != None:
            len += 1
            p = p.next
        if len == 0:
            return head
        k = k % len
        if k == 0:
            return head
        pre = head
        p = head
        dis = 0
        while dis < k:
            p = p.next
            dis += 1
            if p == None:
                return head
        while p.next != None:
            p = p.next
            pre = pre.next
        p.next = head
        head = pre.next
        pre.next = None
        return head


solution = Solution()
k = 3
n = 3
head = ListNode(1)
p = head
for i in range(2,n):
    p.next = ListNode(i)
    p = p.next

head = solution.rotateRight(head, k)
while head != None:
    print head.val,
    head = head.next
