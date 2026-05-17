#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 因为是环, 所以直接拆分, 考虑两种情况, 不偷最后一家 or 不偷第一家
        # 不能分为偷最后一家 or 偷第一家 因为你在dp里面, 偷还是不偷还需要对比确认

        if len(nums) == 1:
            return nums[0]

        def rob_help(nums):

            # dp[i] 偷到 nums[:i]的最大收益

            dp = [0] * (len(nums) + 1)
            # dp[0]是有意义的, 什么都不偷当然是0
            dp[0] = 0
            dp[1] = nums[0]

            for i in range(2, len(nums) + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

            return dp[len(nums)]

        return max(rob_help(nums[1:]), rob_help(nums[:-1]))


# @lc code=end
sol = Solution()
res = sol.rob([2,3])
print(res)
