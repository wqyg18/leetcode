#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
from typing import List


# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 连续上升：只保留最后那个最高点
        # 连续下降：只保留最后那个最低点
        # 方向反转：答案 +1

        prev_diff = 0
        res = 1
        for i in range(1, len(nums)):
            cur_diff = nums[i] - nums[i - 1]
            # 只有第一次遍历时prev_diff = 0, 后续均不为0
            if cur_diff * prev_diff <= 0 and cur_diff != 0:
                res += 1
                prev_diff = cur_diff

        return res


# @lc code=end
sol = Solution()
res = sol.wiggleMaxLength(nums = [1,2,3,4,5,6,7,8,9])
print(res)
