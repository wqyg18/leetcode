#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from typing import List


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False

        dp = [False] * (target + 1)
        dp[0] = True
        # 容量大小为target的背包
        # dp[i]容量恰好为i的背包是否能做到
        for num in nums:
            for i in range(target, num - 1, -1):
                # 拿还是不拿这个num
                # 不拿, 意思是原来就能凑出i
                # 拿， 那么需要看看能不能凑出i - num
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


# @lc code=end
sol = Solution()
res = sol.canPartition(nums=[1,5,11,5])
print(res)
