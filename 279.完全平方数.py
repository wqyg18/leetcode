#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] + [float("inf")] * n

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[-1]


# @lc code=end
sol = Solution()
res = sol.numSquares(8)
print(res)
