#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Double for loop is quite not efficient
        # length = len(height)
        # container = []
        # for i in range(length):
        #     if i < length - 1:
        #         for j in range(1, length - i):
        #             bias = i + j
        #             if height[i] < height[bias]:
        #                 multi = height[i] * j
        #             else:
        #                 multi = height[bias] * j       
        #             container.append(multi)

        # return max(container)

        # If height[L] > height[R], move L, else move R. Say height[0] < height[5], area of (0, 4), (0, 3), (0, 2), (0, 1) must be smaller than (0, 5), hence no need to try them. 
        # Make ends narrow down, store maxArea in res. When narrowing down, compare left and right and update.

        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0 
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        
        return res 
