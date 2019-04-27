#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (40.01%)
# Total Accepted:    271.2K
# Total Submissions: 677.7K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution:
    def countAndSay(self, n: int) -> str:
        """
        :type n: int 
        :rtype: str
        """
        num = "1"
        temp = list(num)
        count = 1
        if n == 1:
            return num
        for i in range(1, n):
            if len(temp) == 1:
                num = "11"
                temp = list(num)
                num = ""
                continue
            for index, value in enumerate(temp):
                if index <= len(temp) - 2:                
                    if temp[index] == temp[index + 1] :
                      count += 1
                    else:
                        num += str(count) + value 
                        count = 1
                if index == len(temp)-1:
                    num += str(count) + value
                    count = 1
            temp = list(num)
            num = ""
        
        num = "".join(temp)    
        return num
                    

