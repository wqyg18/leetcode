#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        path = []
        res = []

        def backtrack(start):
            if len(res) == 2 ** len(nums):
                return

            res.append(path[:])

            for i in range(start, len(nums)):

                # append -> backtrack() -> pop
                # 逻辑是, 先用当前这个填充, 然后backtrack
                # 当前这个填充之后, 该换下一个了, 所以需要pop
                # backtrack就是在当前这个填充之后, 后续一直重复这样的过程
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


# @lc code=end
sol = Solution()
res = sol.subsets(nums=[3, 2, 4, 1])
print(res)
