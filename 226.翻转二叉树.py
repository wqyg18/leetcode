#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        left = root.right
        right = root.left

        root.left = left
        root.right = right

        # 虽然invertTree函数返回了 root, 但是在递归调用的时候, 并没有获取返回值
        # 所以没有影响
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
        
# @lc code=end

