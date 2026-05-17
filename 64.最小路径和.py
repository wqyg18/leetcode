#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        # dp[i][j]: 以(i-1,j-1)下标为终点的最小路径和
        dp[0][1] = 0
        dp[1][0] = 0

        # 判断是否应该多开一圈, 是要看, dp[0][j], dp[i][0]为0, 是否完全符合题意
        # 对于路径题, 如果多开了一圈, 就等于多了一种免费路径, 那么需要初始化为float("inf")
        # 然后留一个入口

        # 强依赖左上角, 正序遍历
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        return dp[m][n]


# @lc code=end
sol = Solution()
res = sol.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
print(res)
