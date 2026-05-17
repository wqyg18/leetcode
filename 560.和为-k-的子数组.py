#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
from typing import List


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 presum
        # 如果 j,,,i 的和为k
        # 那么presum(i) - presum(j-1) = k
        # 即 presum(j-1) = presum(i) - k
        # 遍历到i的时候, 只需要知道前面有几个presum(i) - k就行了

        # 初始化 {0: 1} 是为了处理前缀和正好等于 k 的情况
        hashmap = {0: 1}
        res = 0
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            # 如果 (当前前缀和 - k) 在哈希表中，说明找到了和为 k 的子数组
            if current_sum - k in hashmap:
                res += hashmap[current_sum - k]
            hashmap[current_sum] = hashmap.get(current_sum, 0) + 1
        return res


# @lc code=end
