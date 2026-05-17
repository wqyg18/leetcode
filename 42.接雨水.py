#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import List


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        res = 0

        while left < right:
            # 如果左边低就往右走, 右边低就往左走
            if height[left] < height[right]:
                # 同时往右走的时候, 如果左边已经有更高的了
                # 此时由于有边界更高, 所以left_max - height[left]一定是存的了水的
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1

        return res


# @lc code=end
sol = Solution()
res = sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(res)
