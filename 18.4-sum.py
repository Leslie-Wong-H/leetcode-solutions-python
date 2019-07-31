#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums, target, N, result, results):
            # early termination
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            
            # two pointers solve sorted 2-sum problem
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            
            # recursion, 4sum -> 3sum -> 2sum.
            # fix first number, and in the inner recursion, fix the second number.
            # the more inner recursion, apply 2sum to match the target.
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1 :], target - nums[i], N - 1, result + [nums[i]], results)
                        
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
        
                        


