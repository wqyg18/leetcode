#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        # dp[i] = 偷到第 i 家为止的最大金额, 可以偷i, 也可以不偷
        # dp[n] = dp[n-2] + nums[n]
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
        """
    
        # 其实只用到了dp[n-2], dp[n-1], 因此可以直接使用两个变量代替
        # prev2: dp[n-2]
        # prev1: dp[n-1]

        prev2 = 0
        prev1 = 0

        for num in nums:
            current = max(prev2 + num, prev1)

            prev2 = prev1
            prev1 = current
        
        return prev1

# @lc code=end
sol = Solution()
res = sol.rob([2, 1, 1, 2])
print(res)
