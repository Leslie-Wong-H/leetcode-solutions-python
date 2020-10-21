#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        for item in nums:
            if not numsDict.__contains__(item):
                numsDict[item] = 1
            else:
                numsDict[item] = numsDict[item] + 1
        numsKeysList = list(numsDict.keys())
        numsValuesList = list(numsDict.values())
        return numsKeysList[numsValuesList.index(max(numsValuesList))]
        # @lc code=end
