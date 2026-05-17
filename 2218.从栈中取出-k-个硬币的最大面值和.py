#
# @lc app=leetcode.cn id=2218 lang=python3
#
# [2218] 从栈中取出 K 个硬币的最大面值和
#
from typing import List


# @lc code=start
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # 一共k步, 那么每一步需要决策, 取哪一个pile的值(必须取, 不存在不取的情况)
        # dp[j]: 处理了很多栈, 拿了j次对应的最大面值和
        dp = [0] * (k + 1)

        # 需要遍历每一个栈
        # 需要枚举每一个x, 然后取最大值
        # dp[j] = max(dp[j], dp[j-x] + prefix[x])

        for pile in piles:
            for j in range(k, -1, -1):
                cnt = 0
                
                # 需要注意这里, 可能栈的大小是小于k的
                for x in range(min(j, len(pile))):
                    cnt += pile[x]
                    dp[j] = max(dp[j], dp[j - (x + 1)] + cnt)

        return dp[k]


# @lc code=end
sol = Solution()
res = sol.maxValueOfCoins(piles=[[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k=7)
print(res)
