#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(start):
            if sum(path) == target:
                res.append(path[:])
                # return的意思是, 这一次迭代就结束了,
                # 基于当前情况的, 后续不需要也不能再继续递归了
                return

            if sum(path) > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # 这里backtrack(i)的意思是, 可以继续拿当前这个数字
                # 如果是backtrack(i+1)， 那么就是只能往后一直走， 不能重复使用
                backtrack(i)
                path.pop()

        backtrack(0)
        return res


# @lc code=end

sol = Solution()
res = sol.combinationSum(candidates = [2,3,5], target = 8)
print(res)
