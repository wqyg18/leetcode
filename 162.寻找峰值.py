#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
from typing import List
from bisect import bisect_left


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # logn 那么肯定是二分查找一次
        # 不能直接max(nums), 然后直接二分查找, 因为max是O(n)

        # 那么问题就是, 应该二分查找什么
        # 比较 nums[mid] 和 nums[mid + 1]，往一定存在峰值的那一边走。
        left = 0
        right = len(nums) - 1

        # nums[mid] < nums[mid+1] 证明现在是上坡, 可以一直往右走, 峰值肯定在右边
        # nums[mid] > nums[mid+1] 证明现在是下坡了, 那么这是可能mid就是峰值, 或者还在mid左边

        while left < right:
            mid = left + (right - left)
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end
sol = Solution()
res = sol.findPeakElement(nums=[1, 2, 3, 1])
print(res)
