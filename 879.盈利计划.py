#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#
from typing import List


# @lc code=start
class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        # dp[i][j]代表i名员工, 利润为j的方案数目
        # 只需要在统计的时候, 直接将大于minProfit的算作minProfit

        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        MOD = 10**9 + 7
        for g, p in zip(group, profit):
            for i in range(n, g - 1, -1):
                for j in range(minProfit, -1, -1):
                    # 是否选择当前方案(g, p)
                    new_j = min(minProfit, j + p)
                    # 这里实际是dp[i][j + p] += dp[i - g][j]
                    # 也就是选择当前这个g,p, 对应的方案数 += 不选择这个g,p对应的方案数
                    # 那么遍历所有的g,p, 就是对应的方案数
                    # 因为题目要求，所以直接将大于minProfit的算作minProfit
                    dp[i][new_j] += dp[i - g][j]

        return sum(dp[i][minProfit] for i in range(n + 1)) % MOD


# @lc code=end
sol = Solution()
res = sol.profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8])
print(res)
