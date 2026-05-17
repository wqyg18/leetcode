#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            j = hashmap.get(nums[i], -1)
            if j != -1:
                if abs(i - j) <= k:
                    return True
            hashmap[nums[i]] = i
        return False


# @lc code=end
