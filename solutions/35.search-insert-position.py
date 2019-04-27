#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.63%)
# Total Accepted:    380.6K
# Total Submissions: 936.8K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int 
        :rtype: int 
        """

        if target not in nums:
            nums.append(target)
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                return i


