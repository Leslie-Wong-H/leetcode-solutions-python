#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        """
        The philosophy of this algorithm is to arange the list first, assume the result is the first three numbers in the sorted list, and use another iterable sum to compare. 

        In the first layer of loop, assume the three numbers of sum as the first two and the last in the iterable list.
         
        In the second layer of loop, if sum is smaller than target, increase its middle index, else decrease its last index
        """

        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
        
        return result

