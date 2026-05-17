#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from typing import List


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        # 将nums转成set的复杂度是O(n),但是O(n)+O(n)还是O(n)
        num_set = set(nums)
        length = 1

        for x in num_set:
            if x - 1 not in num_set:
                current_num = x
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                length = max(length, current_length)

        return length


# @lc code=end
