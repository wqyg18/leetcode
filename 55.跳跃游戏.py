#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0 + nums[0]
        if len(nums) == 1:
            return True

        for i in range(1, len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return False


# @lc code=end
sol = Solution()
res = sol.canJump([2, 3, 1, 1, 4])
print(res)
