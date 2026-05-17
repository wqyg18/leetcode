#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from typing import List


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # 很像合并区间的题, 直接左边界排序, 然后更新右边界max

        intervals.append(newInterval)
        # n logn
        intervals.sort(key=lambda x: x[0])
        # 如果用二分差分, logn

        res = []
        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])

            else:
                res[-1][1] = max(res[-1][1], end)

        return res


# @lc code=end
sol = Solution()
res = sol.insert(
    intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
)
print(res)
