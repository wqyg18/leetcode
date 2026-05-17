#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
from typing import List


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # P代表+之和, N代表-之和
        # P - N = target
        # P + N = sum(nums)
        # 2P = target + sum(nums)
        # P = (target + sum(nums)) // 2

        # 即, 凑满容量为P的背包, 方案有多少种

        if sum(nums) < abs(target):
            return 0
        
        p = (target + sum(nums)) // 2

        # P必须是一个整数
        if (target + sum(nums)) % 2 != 0:
            return 0

        dp = [0] * (p + 1)
        dp[0] = 1

        for num in nums:
            for i in range(p, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[p]


# @lc code=end
sol = Solution()
res = sol.findTargetSumWays(nums=[1,1,1,1], target=-1000)
print(res)
