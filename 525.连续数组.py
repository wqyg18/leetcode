#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
from typing import List


# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        # 把0看成-1, 那么相同前缀和就代表, 中间段和为0
        # 0...j, j+1...i
        # 若sum_j = sum_i
        # 那么 j+1...i就是和为0
        # 因此 i - (j + 1) + 1 = i - j

        map = {0: -1}
        # 前缀和: 索引
        sum = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            sum += nums[i]

            if sum not in map:
                map[sum] = i

            else:
                res = max(res, i - map[sum])

        return res


# @lc code=end
