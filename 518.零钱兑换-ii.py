#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
from typing import List


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] amount为i对应的方案数

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                # 等于已经凑出了i - coin的钱, 然后加上coin就是i对应的方案数
                # 只是加上了coin, 方案数不变
                dp[i] += dp[i - coin]

        return dp[amount]


# @lc code=end
sol = Solution()
res = sol.change(amount=5, coins=[1, 2, 5])
print(res)
