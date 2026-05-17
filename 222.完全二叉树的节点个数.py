#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
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
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def getHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        if not root:
            return 0

        left_h = getHeight(root.left)
        right_h = getHeight(root.right)

        if left_h == right_h:
            # 证明left tree是满的, 全是子节点
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # 此时right tree全是子节点
            return (1 << right_h) + self.countNodes(root.left)
        

# @lc code=end
