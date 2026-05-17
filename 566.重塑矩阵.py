#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
from typing import List


# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        res = [[0] * c for _ in range(r)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                idx = i * len(mat[0]) + j
                new_i = idx // c
                new_j = idx % c

                res[new_i][new_j] = mat[i][j]
        return res


# @lc code=end
sol = Solution()
res = sol.matrixReshape(mat=[[1],[2],[3],[4]], r=2, c=2)
print(res)
