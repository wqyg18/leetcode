#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
from typing import List


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[i][j]: 以matrix[i-1][j-1]为右下角的正方形的最大全为1的边长
        # dp[i][j]是1-based

        # 显然强依赖左上的结果 ,需要正序遍历
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return max(max(row) for row in dp) ** 2


# @lc code=end
sol = Solution()
res = sol.maximalSquare(
    matrix=[
        ["0", "0", "0", "1"],
        ["1", "1", "0", "1"],
        ["1", "1", "1", "1"],
        ["0", "1", "1", "1"],
        ["0", "1", "1", "1"],
    ]
)
print(res)
