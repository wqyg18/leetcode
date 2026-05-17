#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 首先遍历i,j, 如果当前是1, 结果+1, 那么递归上下左右, 将1改成0, 这样就找到了这个岛的所有组成部分

        def dfs(i, j):
            # 这里应该限制的是, i,j是正确取值就可以了, 也就是不会索引越界
            # 因为周围是海, 只要是1就可以是岛屿
            if i < 0 or i > len(grid) - 1:
                return
            if j < 0 or j > len(grid[0]) - 1:
                return

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # 找到1, 然后让周围所有相连的1变成0
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res


# @lc code=end
sol = Solution()
res = sol.numIslands(
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)
print(res)
