#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 非递减 : 递增但是可以相等

        def find_left() -> List[int]:
            # 找到第一个target
            left, right = 0, len(nums) - 1
            res = float("inf")
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return res if res != float("inf") else -1

        def find_right() -> List[int]:
            # 找到最后一个target
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return res

        return [find_left(), find_right()]


# @lc code=end
