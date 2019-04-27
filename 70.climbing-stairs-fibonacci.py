#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        : type n: int 
        : rtype: int 
        """
        pre = 0
        prepre = 1
        sum = 0
        for fibonacci in range(n+1):
            fibonacci = pre
            sum = fibonacci + prepre
            prepre = pre
            pre = sum
        return sum
