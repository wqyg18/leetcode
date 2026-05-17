#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 记录一个最远距离, 然后每次i==max_reach的时候, 跳一次
        max_reach = 0
        cur_end = 0
        step = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            # 相当于是, 每一步, 遍历然后找到max_reach
            # 然后到达上一次的max_reach, 就是一个step
            if i == cur_end:
                step += 1
                cur_end = max_reach
        return step


# @lc code=end
sol = Solution()
res = sol.jump([2, 3, 1, 1, 4])
print(res)
