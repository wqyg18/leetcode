#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        # dp[i] 爬到下标 i-1阶
        dp[0] = 1  # 什么都不爬, 当然是1种情况
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# @lc code=end
sol = Solution()
res = sol.climbStairs(n=1)
print(res)
