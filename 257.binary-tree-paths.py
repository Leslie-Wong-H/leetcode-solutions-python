#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (45.63%)
# Likes:    877
# Dislikes: 67
# Total Accepted:    226.4K
# Total Submissions: 492.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        self.finalAns = []
        self.dfs(node=root, l=[])
        for i in range(len(self.ans)):
            s = ''
            for j in range(len(self.ans[i]) - 1):
                s += str(self.ans[i][j]) + '->'
            s += str(self.ans[i][len(self.ans[i]) -1])
            self.finalAns.append(s)
        return self.finalAns
        
    
    def dfs(self, node, l):
        if node is None:
            return
        if node.left is None and node.right is None:
            l.append(node.val)
            self.ans.append(l.copy())
            l.pop()
            return
        l.append(node.val)
        self.dfs(node=node.left, l=l.copy())
        self.dfs(node=node.right, l=l.copy())

    #still traffic function, not run until the previous function end. Need it to return !
    # l is copied, not the original l
    # self.array is a good tool



