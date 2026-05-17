#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心: 用i天的price 减去 0...i-1天的最低price
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


# @lc code=end

