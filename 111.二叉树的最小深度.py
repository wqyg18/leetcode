#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 没了, 当然是0
        if not root:
            return 0

        # 是叶子结点, 计数+1
        if not root.left and not root.right:
            return 1

        # 因为是最小深度, 但是不能让空节点干扰
        # 上面的判断保证了一定有至少一个孩子
        # 如果只有一个孩子的话, 那么没有的那一个需要是inf, 不然会影响
        left = self.minDepth(root.left) if root.left else float("inf")
        right = self.minDepth(root.right) if root.right else float("inf")

        return 1 + min(left, right)


# @lc code=end
