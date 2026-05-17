#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
                continue

            # start < res[-1][1]
            res[-1][1] = max(res[-1][1], end)

        return res


# @lc code=end
sol = Solution()
res = sol.merge([[1, 4], [4, 5]])
print(res)
