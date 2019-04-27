#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.25%)
# Total Accepted:    438.7K
# Total Submissions: 1.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        if len(strs) == 0:
            return common
        
        temp = strs[0]

        for word in strs:
            if len(word) < len(temp):
                temp = word
        
        for i in range(len(temp)):
            for j in range(len(strs)):
                if temp[i] != strs[j][i]:
                    return common
            common += temp[i]

        return common

        

