#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]


# @lc code=end
sol = Solution()
res = sol.combinationSum4(nums=[1, 2, 3], target=4)
print(res)
