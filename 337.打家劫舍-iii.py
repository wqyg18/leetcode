#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
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
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]):
            # [不偷当前节点的最大值, 偷当前节点的最大值]
            if node is None:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            dp0 = max(left) + max(right)
            dp1 = node.val + left[0] + right[0]

            return [dp0, dp1]

        return max(dfs(root))


# @lc code=end
