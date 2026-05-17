#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 最长路径的起点和终点必定是叶子结点

        res = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # 当前节点作为拐点的直径
            res = max(res, left_depth + right_depth)

            # 返回给父节点的是：当前节点向下的最大深度
            return max(left_depth, right_depth) + 1

        dfs(root)
        return res


# @lc code=end
