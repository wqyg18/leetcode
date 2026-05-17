#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow


# @lc code=end
sol = Solution()
k = sol.removeElement([3, 2, 2, 3], 3)
print(k)
