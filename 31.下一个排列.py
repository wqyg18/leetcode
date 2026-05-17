#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 1. 从后往前找第一个 nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. 如果找到了支点，找右边第一个比 nums[i] 大的数交换
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3. 反转后缀
        nums[i + 1:] = reversed(nums[i + 1:])


# @lc code=end
