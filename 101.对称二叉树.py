#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def compare(left: Optional[TreeNode], right: Optional[TreeNode]):
            # 两边都空
            if not left and not right:
                return True

            # 只有一个孩子
            if not left and right:
                return False
            if not right and left:
                return False

            # 有两个孩子
            # 并且值不相等
            if left.val != right.val:
                return False
            
            # 有两个孩子
            # 并且值相等
            # 那么开始递归对比子树
            
            # 注意题目要求是是否互为镜像
            # 所以对比的应该是 最外层的两个一组 最内层的两个一组
            return compare(left.left, right.right) and compare(left.right, right.left)

        if not root:
            return True
        return compare(root.left, root.right)


# @lc code=end
