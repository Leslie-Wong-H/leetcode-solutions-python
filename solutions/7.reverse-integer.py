#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.23%)
# Total Accepted:    652.8K
# Total Submissions: 2.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        """
        :type x: int 
        :rtype: int 
        """
        if x > 0:
            num = str(x)[::-1]
        elif x < 0:
            num = '-' + str(-x)[::-1]
        else:
            return 0 
        
        if int(num) < 2 ** 31 and int(num) >= - 2 ** 31:
            return int(num)
        else:
            return 0
    

