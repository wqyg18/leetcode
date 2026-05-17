#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        left = 0
        right = len(height) - 1
        while left < right:
            current_area = (right - left) * min(height[left], height[right])

            res = max(res, current_area)

            # 核心是移动 短板 对应的那个指针
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        
        return res


# @lc code=end
