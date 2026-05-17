#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from typing import List


# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 缺失的正整数肯定是在1~n之间
        # 我们让k放到下标k-1的位置

        for i in range(n):
            # 对于有用的数, 交换, 让他去到自己应该去的下标
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 如果下标k-1的值不是k, 那么直接return k
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果前面没有return, 证明正好全部符合, 直接return n + 1
        return n + 1


# @lc code=end
sol = Solution()
res = sol.firstMissingPositive([1])
print(res)
