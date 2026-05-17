#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 只要left<root<right 就可以了
        # 需要枚举每一层的节点

        # 例如整棵树的root是2, 那么左子树可选的是[1,2-1], 右子树是[2+1, n]
        # 所以dfs需要传入[left,right]

        def dfs(left, right):
            # 首先判断结束
            # 如果没有数字可用, 那么这棵子树是空的
            if left > right:
                return [None]
            trees = []

            # 枚举每一个可能的数字
            for root_val in range(left, right + 1):
                # 注意dfs传入的(left, right)事都可以取到的两个数字
                left_trees = dfs(left, root_val - 1)
                right_trees = dfs(root_val + 1, right)

                # 合并左右子树
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        trees.append(root)

            return trees

        return dfs(1, n)


# @lc code=end
sol = Solution()
res = sol.generateTrees(n = 3)
print(res)