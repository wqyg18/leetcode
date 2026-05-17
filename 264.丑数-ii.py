#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        p2 = p3 = p5 = 0

        for i in range(1, n):
            num2 = dp[p2] * 2
            num3 = dp[p3] * 3
            num5 = dp[p5] * 5

            dp[i] = min(num2, num3, num5)

            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[-1]
# @lc code=end

