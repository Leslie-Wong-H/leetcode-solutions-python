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
        count = 0
        product1 = 1
        product2 = 1
        product3 = 1
        m = n //2     
        for item in range(1, m + 1):
            Holes = n - 2 * item + item
            for opperand1 in range(1, item + 1):
                product1 *= opperand1
            
            for opperand2 in range(1, Holes + 1):
                product2 *= opperand2
            
            remain = Holes - item
            for opperand3 in range(1, remain + 1):
                product3 *= opperand3
            count += product2 / (product3 * product1)
            product1 = 1
            product2 = 1
            product3 = 1
        count += 1
        return int(count)               
            
                

            
