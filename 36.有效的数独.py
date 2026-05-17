#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from typing import List


# @lc code=start
class Solution:
    # 应该改成使用set(), 判断就是 if current in row
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [dict() for _ in range(9)]
        grids = [dict() for _ in range(9)]

        for i in range(9):
            row = dict()
            for j in range(9):
                current = board[i][j]

                if current == ".":
                    continue

                # 查询i行
                if row.get(current, 0):
                    return False
                row[current] = 1

                # 查询j列
                if cols[j].get(current, 0):
                    return False
                cols[j][current] = 1

                # 查询块
                grid_i, grid_j = i // 3, j // 3
                grid_idx = grid_i * 3 + grid_j
                if grids[grid_idx].get(current, 0):
                    return False
                grids[grid_idx][current] = 1

        return True


# @lc code=end
