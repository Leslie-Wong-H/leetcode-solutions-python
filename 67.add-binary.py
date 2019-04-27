#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.56%)
# Total Accepted:    290.4K
# Total Submissions: 752.9K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        if a == "0" and b != "0":
            return b
        if a != "0" and b == "0":
            return a 
        
        a = a[::-1]
        a_list = list(a)
        b = b[::-1]
        b_list = list(b)
        a_value = 0
        b_value = 0

        for index, value in enumerate(a_list):
            a_value += int(value) * (2 ** index)

        for index, value in enumerate(b_list):
            b_value += int(value) * (2 ** index)

        sum = a_value + b_value

        sum_list = []

        divide = int(sum / 2)

        while divide > 0:
            item = sum % 2
            sum = sum // 2
            sum_list.append(str(item))
            divide = int(divide / 2)
        
        if sum % 2 == 1 and int (sum / 2) == 0:
            sum_list.append('1')
        
        sum_str = "".join(sum_list[::-1])

        return sum_str

