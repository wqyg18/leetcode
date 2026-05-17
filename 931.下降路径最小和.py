#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#
from typing import List


# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[float("inf")] * (n + 2) for _ in range(m + 1)]  # 1-based
        # 本题比较特殊, 出发点是第一行的任意位置, 而不是必须左上角, 所以初始化需要注意
        for i in range(n + 1):
            dp[0][i] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 尽管依赖的是j+1, 但是是上一行的, 已经处理过了
                dp[i][j] = (
                    min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
                    + matrix[i - 1][j - 1]
                )

        return min(dp[m])


# @lc code=end
sol = Solution()
res = sol.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]])
print(res)
