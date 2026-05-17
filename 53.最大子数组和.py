#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        # dp[i] ==> 以下标i结尾的数组的最大和
        dp = [nums[0]] + [None] * (len(nums) - 1)
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])

        return res
        """

        # 最大子数组和 要么在左边, 要么右边, 要么包含中间(mid)
        # mid的情况, 从mid开始, 往左往右分别遍历, 找到最大和
        def dfs(l, r):
            if l == r:
                return nums[l]

            mid = (l + r) // 2
            left = dfs(l, mid)
            right = dfs(mid + 1, r)

            s = 0
            leftmax = nums[mid]
            for i in range(mid, l - 1, -1):
                s += nums[i]
                leftmax = max(leftmax, s)

            s = 0
            rightmax = nums[mid + 1]
            for i in range(mid + 1, r + 1, 1):
                s += nums[i]
                rightmax = max(rightmax, s)

            cross = leftmax + rightmax

            return max(left, right, cross)

        return dfs(0, len(nums) - 1)


# @lc code=end
sol = Solution()
res = sol.maxSubArray([1])
print(res)
