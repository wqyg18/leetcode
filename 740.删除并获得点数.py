#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#
from collections import Counter
from typing import List
import copy


# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        points = [0] * (max(nums) + 1)

        # 题目中num >= 1
        for num, cnt in counter.items():
            points[num] = num * cnt

        # 从小到大, 取到i时候的收益
        # 长度是max(nums) + 1, 包含了0
        dp = [0] * (max(nums) + 1)
        dp[1] = points[1]

        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 2] + points[i], dp[i - 1])

        return dp[-1]


# @lc code=end

sol = Solution()
res = sol.deleteAndEarn([3,4,2])
print(res)
