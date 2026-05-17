#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 1.当前节点能不能作为最近公共祖先
        # 2.如果不能, 应该往上返回什么

        # 在以 node 为根的子树里，如果找到了 p 或 q，就把那个节点往上返回；
        # 如果左右子树分别找到了 p 和 q，说明当前 node 就是最近公共祖先。

        def dfs(node: "TreeNode"):
            if not node:
                return

            if node == q or node == p:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if not left and not right:
                return

            if left and right:
                return node

            if left and not right:
                return left
            if right and not left:
                return right

        return dfs(root)


# @lc code=end
