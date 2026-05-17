#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from typing import List


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] : 以 nums[i] 作为结尾的最长递增子序列长度
        dp = [1] * (n)

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# @lc code=end
sol = Solution()
res = sol.lengthOfLIS([10,9,2,5,3,7,101,18])
print(res)
