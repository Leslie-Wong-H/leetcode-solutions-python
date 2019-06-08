#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    
    # #dfs recursively
    #     res = []
    #     self.dfs(root, 0, res)
    #     return res
    # def dfs(self, root, level, res):
    #     if root:
    #         if len(res) < level + 1:
    #             res.insert(0, [])
    #         res[-(level + 1)].append(root.val)
    #         self.dfs(root.left, level + 1, res)
    #         self.dfs(root.right, level + 1, res)

    # bfs + stack
        # stack = [(root, 0)]
        # res = []
        # while stack:
        #     node, level = stack.pop()
        #     if node:
        #         if len(res) < level + 1:
        #             res.insert(0, [])
        #         res[-(level + 1)].append(node.val)
        #         stack.append((node.right, level + 1))
        #         stack.append((node.left, level + 1))
        # return res
    
    #　bfs + queue
        queue = collections.deque([(root, 0)])
        res = []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res

        


            

