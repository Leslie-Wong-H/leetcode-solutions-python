#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Sum first, then mod ten
        # sumLinkedList = ListNode(0)
        # firstAddend = 0
        # secondAddend = 0
        # exponent = 0
        # while l1 != None:
        #     firstAddend += l1.val * (10 ** exponent)
        #     exponent += 1
        #     l1 = l1.next
        # exponent = 0
        # while l2 != None:
        #     secondAddend += l2.val * (10 ** exponent)
        #     exponent += 1
        #     l2 = l2.next
        # tempSum = firstAddend + secondAddend
        # tempTempSum = tempSum
        # exponent = 1
        # headSumLinkedList = sumLinkedList
        # endIndicator = False
        # while endIndicator == False:
        #     if tempSum >= 10:
        #         digit = tempSum % 10
        #         tempSum = tempSum // 10
        #         sumLinkedList.val = digit
        #         sumLinkedList.next = ListNode(0)
        #         sumLinkedList = sumLinkedList.next
        #     else:
        #         digit = tempSum
        #         sumLinkedList.val = digit
        #         sumLinkedList.next = None
        #         endIndicator = True
        #     exponent += 1
        # return headSumLinkedList

        # Leetcode official
        sumLinkedList = ListNode(0)
        headSumLikedList = sumLinkedList
        carry = 0
        p = l1
        q = l2
        while p != None or q != None:
            if p == None:
                x = 0
            else:
                x = p.val
            if q == None:
                y = 0
            else:
                y = q.val
            sum = x + y + carry
            carry = sum // 10
            tempSum = sum % 10
            sumLinkedList.val = tempSum
            # if both p.next and q.next None, do not add node
            if (p and p.next) or (q and q.next):
                sumLinkedList.next = ListNode(0)
                sumLinkedList = sumLinkedList.next
            p = p.next if p and p.next else None
            q = q.next if q and q.next else None
        if carry == 1:
            sumLinkedList.next = ListNode(carry)
        return headSumLikedList
        # @lc code=end
