#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # deal with array with only one element
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # left to right, and break
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i] < nums[i + 1]:
                    if nums[i] == target:
                        return i
                elif nums[i + 1] == target:
                    return i + 1            
                else:
                    break
                
        # right to left, and break 
        for j in range(len(nums) - 1, 0, -1):
            if j - 1 >= 0:
                if nums[j] > nums[j - 1]:
                    if nums[j] == target:
                        return j
                elif nums[j - 1] == target:
                    return j - 1
                else:
                    break

        return -1


                

