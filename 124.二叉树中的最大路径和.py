#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 相关思想:
        # 往父节点返回什么
        # 能不能在当前节点更新全局答案

        res = -float("inf")

        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # 当前节点作为拐点
            # 结果等于, val+左边的最大值+右边的最大值
            res = max(res, node.val + left + right)

            # 给父节点返回
            return max(left, right) + node.val

        dfs(root)
        return res


# @lc code=end
