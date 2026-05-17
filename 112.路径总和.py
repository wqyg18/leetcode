#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    # 必须是从根节点到叶子结点
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target):
            # 已经是叶子结点了, 没有孩子, 这时还没有达到目标
            if not root:
                return False

            # 现在是叶子结点, 判断一下是否达成目标
            if not root.left and not root.right:
                return target == root.val

            left = dfs(root.left, target - root.val)
            right = dfs(root.right, target - root.val)

            return left or right

        return dfs(root, targetSum)


# @lc code=end
