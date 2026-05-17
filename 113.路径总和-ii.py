#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
from typing import Optional, List


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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        res = []

        def dfs(node: Optional[TreeNode], target):
            if not node:
                return

            path.append(node.val)

            # 如果是叶子结点
            if not node.left and not node.right:
                if target == node.val:
                    res.append(path[:])
            # 不是叶子结点
            else:
                dfs(node.left, target - node.val)
                dfs(node.right, target - node.val)

            path.pop()

        dfs(root, targetSum)
        return res


# @lc code=end
