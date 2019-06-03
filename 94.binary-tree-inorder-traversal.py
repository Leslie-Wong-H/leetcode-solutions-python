#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (56.13%)
# Likes:    1605
# Dislikes: 71
# Total Accepted:    463K
# Total Submissions: 816.5K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # Method 1:

        # self.result = []
        # stack = []
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         root = stack.pop()
        #         result.append(root.val)
        #         root = root.right
        # return result

        # Method 2:

        self.result = []
        self.inorderInsert(root)
        return self.result
    
    def inorderInsert(self, node):
        if node is None:
            return
        self.inorderInsert(node=node.left)
        self.result.append(node.val)
        self.inorderInsert(node=node.right)


        

