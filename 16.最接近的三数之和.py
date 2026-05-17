#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(target - s) < abs(target - best):
                    best = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                elif s == target:
                    return s

        return best


# @lc code=end
