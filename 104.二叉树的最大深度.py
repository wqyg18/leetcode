#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # 先确定递归结束条件
        if not root:
            return 0

        # 递归遍历left, right
        # 当前节点, 遍历过了, 所以+1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# @lc code=end
