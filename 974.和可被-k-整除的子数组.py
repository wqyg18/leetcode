#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
from typing import List


# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 前缀和
        # 0...j,j+1...i
        # 如果 sum_i的余数 和 sum_j 的余数相同
        # 则 j+1...i可以被k整除

        res = 0
        sum = 0
        # 初始化0:1, 是为了[k]这种情况
        sum_map = {0: 1}
        for i in range(len(nums)):
            sum += nums[i]
            remainder = sum % k

            res += sum_map.get(remainder, 0)

            if remainder in sum_map:
                sum_map[remainder] += 1
            else:
                sum_map[remainder] = 1

        return res


# @lc code=end
