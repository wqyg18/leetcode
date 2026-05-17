#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除了自身以外数组的乘积
#
from typing import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 3个for loop的时间复杂度也是O(n)
        res = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


# @lc code=end

sol = Solution()
res = sol.productExceptSelf([-1, 1, 0, -3, 3])
print(res)
