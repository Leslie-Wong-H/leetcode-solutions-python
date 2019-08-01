#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Lexicographical order: arrange word according to the alphabet sequence, for example, 'an' is arranged before 'as'."""
        
        # Slution: Find from right to left, move left if in ascending order,
        #  stop when not ascend. Converse the found sequence,
        # and then compare the number left to stop index with numbers in the found sequence,
        # swap it with the least bigger one.
        # Another thought: the righteat digit has the least value in determine order, and the leftest digit has the biggest value in determin order. 
        # assume nums = [3, 4, 5. 2, 1]
        
        if len(nums) < 2:
            return
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # nums = [3, 4, 1, 2, 5] 
        
        k = i - 1
        for j in range(i, len(nums)):
            if nums[j] > nums[k]:
                nums[j], nums[k] = nums[k], nums[j]
                break
        # nums = [3, 5, 1, 2, 4]


