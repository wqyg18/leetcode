#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
from typing import List


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 仍旧是岛屿数量的思路, 只不过在dfs的时候, 实时增加面积

        def dfs(i, j):
            if i < 0 or i > len(grid) - 1:
                return 0
            if j < 0 or j > len(grid[0]) - 1:
                return 0

            if grid[i][j] == 0:
                return 0

            # 当前是陆地
            grid[i][j] = 0

            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # 找到1, 然后让周围所有相连的1变成0
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res


# @lc code=end
sol = Solution()
res = sol.maxAreaOfIsland(
    grid=[
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    ]
)
print(res)
