#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start


class Solution:
    def jump(self, nums: List[int]) -> int:
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            # in case value == 1
            maxend = end + 1
            for i in range(start, end + 1):
                # index matters. index is connected with the corresponding value
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
            # every index with its value could lead to the final step. Watch out! -- i + nums[i]
        return step
        # @lc code=end
