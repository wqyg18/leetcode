#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
from typing import List


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 依旧岛屿, 但是正向不是很好处理
        # 反向, 从边界开始, 如果是'O', 那么肯定不是被围绕的
        # 找到所有的非被围绕的, 剩下的全部都是围绕的

        # 找到所有和边界 O 连通的 O，标记为 visited
        # visited 表示：这个 O 是安全的，不能被翻转
        # 最后没被 visited 标记的 O，说明被 X 包围，要变成 X

        def dfs(i, j):
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[0]):
                return

            if board[i][j] != "O":
                return

            if visited[i][j]:
                return

            # 处理
            visited[i][j] = True

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        visited = [[False] * len(board[0]) for _ in range(len(board))]

        m, n = len(board), len(board[0])
        # 只从边界 O 出发
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visited[i][j]:
                    board[i][j] = "X"


# @lc code=end
