#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        candidates.sort()

        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                # i > start 确保了 i - 1 一定有效
                # 也就是只从第二个开始对比是否重复
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # 剪枝
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])
                path.pop()

        backtrack(0, target)
        return res


# @lc code=end
sol = Solution()
res = sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
print(res)
