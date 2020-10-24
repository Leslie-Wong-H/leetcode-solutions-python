#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # # Vanilla List Version:
        # tempList = []
        # if head == None:
        #     return head
        # while head and head.next:
        #     tempList.append(head.val)
        #     head = head.next
        # tempList.append(head.val)
        # tempList.reverse()
        # linkNodeHead = ListNode(tempList[0])
        # originalLinkNodeHead = linkNodeHead
        # for item in tempList[1:]:
        #     nextLinkNodeHead = ListNode(item)
        #     linkNodeHead.next = nextLinkNodeHead
        #     linkNodeHead = linkNodeHead.next
        # return originalLinkNodeHead

        # Elegant Version, Reverse step by step：
        if head == None:
            return head
        formerlinkNodeHead = ListNode(head.val)
        head = head.next
        while head and head.next:
            latterlinkNodeHead = ListNode(head.val)
            latterlinkNodeHead.next = formerlinkNodeHead
            formerlinkNodeHead = latterlinkNodeHead
            head = head.next
        # The end node
        if head:
            latterlinkNodeHead = ListNode(head.val) 
            latterlinkNodeHead.next = formerlinkNodeHead
            formerlinkNodeHead = latterlinkNodeHead
        return formerlinkNodeHead
# @lc code=end
