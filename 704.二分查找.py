#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import List


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [left, right]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 由于找到就return, 所以left,right均不需要保留
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


# @lc code=end
