#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#


# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1] + [None] * (n - 1)

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# @lc code=end
sol = Solution()
res = sol.fib(4)
print(res)
