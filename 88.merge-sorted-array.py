#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index in range(m):
            nums2.append(nums1[index])
        nums2 = sorted(nums2)
        for index in range(m + n):
            nums1[index] = nums2[index]
            
        

