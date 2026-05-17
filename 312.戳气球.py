#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
from typing import List


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] : nums[i:j]对应的结果
        nums = [1] + nums + [1]
        n = len(nums)

        # 首先nums已经补齐了边界

        dp = [[0] * n for _ in range(n)]

        # 这里倒序遍历，是因为， dp[left][right]依赖dp[k][right], 而k>left
        for left in range(n - 1, -1, -1):
            # 起码要三个元素, 所以是left+2
            for right in range(left + 2, n):
                # 需要遍历所有的最后一个戳破的气球
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        # k作为右端点的，k作为左端点的，戳K的值
                        dp[left][k] + dp[k][right] + nums[left] * nums[k] * nums[right],
                    )

        return dp[0][n - 1]


# @lc code=end
sol = Solution()
res = sol.maxCoins(nums=[3, 1, 5, 8])
print(res)
