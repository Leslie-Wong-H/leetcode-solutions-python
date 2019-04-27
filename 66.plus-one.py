#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (40.93%)
# Total Accepted:    371.7K
# Total Submissions: 908K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # num = int("".join([str(x) for x in digits])) + 1
        # num = [int(x) for x in str(num)]
        i = len(digits)
        sum = 0
        for num in range(i):
            if num != i-1:
                temp = digits[num]*(10**(i-num-1))
                sum += temp
        sum += digits[i - 1]
        sum += 1
        new_list = [int(x) for x in str(sum)]      
        return new_list
        

