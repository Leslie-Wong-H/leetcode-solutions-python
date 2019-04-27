#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.21%)
# Total Accepted:    256.4K
# Total Submissions: 796K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# Input: "Hello World"
# Output: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        :type s: str
        :rtype: int 
        """
        if len(s) == 0:
            return 0
        
        s_split = s.split(" ")

        for word in s_split[::-1]:
            if len(word) > 0:
                return len(word)
        return 0 

