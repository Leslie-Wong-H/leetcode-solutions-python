#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, index, path, res):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(nums)):
                dfs(nums, target - nums[i], i, path + [nums[i]], res)
                

        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res
        #  What a wonderful recursion method 

        