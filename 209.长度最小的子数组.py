#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import List


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 0...j,j+1...i

        res = float("inf")

        left = 0
        current_sum = 0
        for right in range(0, len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                res = min(res, right - left + 1)
                current_sum -= nums[left]
                left += 1

        # 证明没有target
        if res != float("inf"):
            return res
        else:
            return 0


# @lc code=end
sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen(4, [1, 4, 4]))
print(sol.minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(sol.minSubArrayLen(6, [10]))
print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
