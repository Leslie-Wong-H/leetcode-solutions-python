#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, index, path, res): 
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index + 1 , len(nums)):
                dfs(nums, target - nums[i], i, path + [nums[i]], res)
        
        res = []
        candidates.sort()
        for i in range(len(candidates)):
            dfs(candidates, target - candidates[i], i,  [candidates[i]], res)
        
        # remove duplicate combinations
        reres = list(set([tuple(t) for t in res]))

        return reres



