#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
from typing import List


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # (i, j) → (j, n - 1 - i)
        # 即转置+行反转
        n = len(matrix)

        # 只需要1.转置 2.每一行行=reverse

        # 注意只转置上三角或下三角
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


# @lc code=end
