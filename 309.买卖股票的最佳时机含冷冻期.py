#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # hold: 第 i 天结束后，手里持有股票的最大利润
        # sold: 第 i 天结束后，今天刚卖出股票的最大利润
        # rest: 第 i 天结束后，手里没股票，且今天没有卖出的最大利润

        hold = [0] * n
        sold = [0] * n
        rest = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            # 今天有股票, 1:昨天就已经有了, 2: 今天买的, 但是要求昨天是rest
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])

            # 今天卖出, 要求昨天持有
            sold[i] = hold[i - 1] + prices[i]

            # 今天休息, 1: 昨天卖出了, 2:无事发生
            rest[i] = max(sold[i - 1], rest[i - 1])

        # 1:最后一天卖的, 2:之前就已经卖了, 且后续没有买入
        return max(rest[n - 1], sold[n - 1])


# @lc code=end
sol = Solution()
res = sol.maxProfit(prices=[1])
print(res)
