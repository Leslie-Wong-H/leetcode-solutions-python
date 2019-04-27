#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        current = head
        newHead = ListNode(0)
        newcurrent = newHead
        newcurrent.next = current
        newcurrent = newcurrent.next
        while current != None and current.next != None:
            if current.val == current.next.val:
                current = current.next
                if current.next == None:
                    newcurrent.next = None
                continue
            else:
                current = current.next
                newcurrent.next = current
                newcurrent = newcurrent.next
        return newHead.next





