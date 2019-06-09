#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # Method1 recursive

        # self.flag = True

        # def maxDepth(root):

        #     if not root:
        #         return 0
                
        #     leftDepth  = maxDepth(root.left)
        #     rightDepth = maxDepth(root.right)
            
        #     if abs(leftDepth - rightDepth) > 1:
        #         self.flag = False
        #     return 1 + max(leftDepth, rightDepth)

        # maxDepth(root)
        # if self.flag == False:
        #     return False
        # else:
        #     return True

        # Method2 iterative

        stack = []
        node = root
        last = None
        depths = {}
        

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        
        return True



