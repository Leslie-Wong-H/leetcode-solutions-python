#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True
        # For me, 1, 2, 3, I win; 4, I lose;
        # 5,6,7, leave it to 1,2,3, I win; 8, my enemy gets 5,6,7, I lose;
        # etc. 
# @lc code=end

