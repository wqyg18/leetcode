#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            # 必须要先检查, 再存入
            if (target - nums[i]) in hashmap:
                return i, hashmap[target - nums[i]]
            hashmap[nums[i]] = i


# @lc code=end
