#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.22%)
# Total Accepted:    556.3K
# Total Submissions: 1.5M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str 
        :rtype: bool
        """
        brackets_dict = {"(": ")", "[": "]", "{": "}"}
        str_list = list(s)
        result = []
        brackets_list = []

        for bracket in str_list:
            if bracket not in brackets_dict:
                brackets_list.append(bracket)
            if bracket in brackets_dict:
                result.append(bracket)
            if len(result) > 0:
                if bracket == brackets_dict[result[-1]]:
                    result.pop(-1)
                    brackets_list.remove(bracket)

        if len(result) > 0 or len(brackets_list) > 0:
            return False
        else:
            return True
            

