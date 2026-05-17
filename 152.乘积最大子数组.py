#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from typing import List


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 对于最大乘积的问题, 因为同时存在正数和负数, 所以只维护最大值不行, 还需要维护最小值

        # max_dp: 以当前元素结尾的最大乘积
        # min_dp: 以当前元素结尾的最小乘积
        max_dp = nums[0]
        min_dp = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            prev_max = max_dp
            prev_min = min_dp

            max_dp = max(x, prev_max * x, prev_min * x)
            min_dp = min(x, prev_max * x, prev_min * x)

            res = max(res, max_dp)

        return res


# @lc code=end
sol = Solution()
res = sol.maxProduct(nums=[-2, 3, -4])
print(res)
