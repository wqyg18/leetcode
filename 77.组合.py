#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                if i in path:
                    continue

                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res


# @lc code=end
sol = Solution()
res = sol.combine(n=4, k=2)
print(res)
