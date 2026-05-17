#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
from typing import List


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 确定只存在一个岛屿

        # 找到第一个1, 然后走到水, 那么+1
        # 边界也是水, 那么走到边界也要+1

        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 1
            if j < 0 or j >= len(grid[0]):
                return 1

            if grid[i][j] == 0:
                return 1

            # 已经走过了
            if grid[i][j] == 2:
                return 0

            # 需要标记一下, 这个点已经走过了
            grid[i][j] = 2

            return dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 找到第一个1, 然后dfs直接遍历完所有的岛屿了
                # 直接break
                if grid[i][j] == 1:
                    res = dfs(i, j)
                    break
        return res


# @lc code=end
sol = Solution()
res = sol.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
print(res)
