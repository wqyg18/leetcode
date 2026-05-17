#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from typing import List


# @lc code=start
class Solution:
    # 注意审题, 本体要求是自顶向下, 只要到最后一层就可以了, 并不是非要到最后一列
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]  # 1-based
        # dp[i][j] 到达triangle[i-1][j-1]的最下路径和
        dp[0][0] = 0
        dp[0][1] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j > i:
                    break
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i - 1][j - 1]

        return min(dp[m])


# @lc code=end
sol = Solution()
res = sol.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print(res)
