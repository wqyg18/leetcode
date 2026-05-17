#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # 整体reverse, 然后前k和后K分别reverse
        def my_reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1

        my_reverse(0, n - 1)
        my_reverse(0, k - 1)
        my_reverse(k, n - 1)


# @lc code=end
sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums, 3)
print(nums)
