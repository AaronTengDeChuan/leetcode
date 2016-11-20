#!usr/bin/env python
#-*-coding:utf-8-*-
import sys 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        tmp = ListNode(0)
        tmp.next = head
        p = head
        pre = tmp
        cur = head.val
        flag = False
        while p != None:
            while p.next != None and p.next.val == cur:
                flag = True
                p = p.next
            if flag:
                pre.next = p.next
                flag = False
            else:
                pre = p
            p = p.next
            if p != None:
                cur = p.val
        return tmp.next

solution = Solution()
head = ListNode(1)
p = head
p.next = ListNode(1)
p = p.next
p.next = ListNode(1)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(5)
p = p.next
p.next = ListNode(5)
head = solution.deleteDuplicates(head)
p = head
while p != None:
    print p.val,
    p = p.next


