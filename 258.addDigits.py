#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # My solution:
        digitalizedNum = [int(item) for item in list(str(num))]
        sumDigitalizedNum = sum(digitalizedNum)
        while sumDigitalizedNum >= 10:
            digitalizedNum = [int(item)
                              for item in list(str(sumDigitalizedNum))]
            sumDigitalizedNum = sum(digitalizedNum)
        return sumDigitalizedNum
        # Reference solution (wonderful math trick):
        # return num if num == 0 else num % 9 or 9

        # @lc code=end
