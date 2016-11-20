#usr/bin/env python
#-*-coding:utf-8-*-
import sys
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def binaryMergeSort(self, head, len):
        if len == 0 or len == 1:
            return head
        left_len = len / 2
        right_len = len - len / 2
        left = head
        for i in range(left_len):
            head = head.next
        right = head
        head = ListNode(0)
        p = head
        left = self.binaryMergeSort(left, left_len)
        right = self.binaryMergeSort(right, right_len)
        while left_len > 0 and right_len > 0:
            if left.val < right.val:
                p.next = left
                p = p.next
                left = left.next
                left_len -= 1
            else:
                p.next = right
                p = p.next
                right = right.next
                right_len -= 1
        while left_len:
            p.next = left
            p = p.next
            left = left.next
            left_len -= 1
        while right_len:
            p.next = right
            p = p.next
            right = right.next
            right_len -= 1
        p.next = None
        return head.next



    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        len = 0
        while p != None:
            len += 1
            p = p.next
        head = self.binaryMergeSort(head, len)
        return head

solution = Solution()
head = ListNode(5)
p = head
p.next = ListNode(4)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(2)
p = p.next
p.next = ListNode(1)
head = solution.sortList(head)
while head != None:
    print head.val,
    head = head.next


        
