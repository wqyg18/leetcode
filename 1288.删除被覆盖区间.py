#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#
from typing import List


# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 一个区间 被 另一个区间完全覆盖
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            # 全覆盖
            if end <= max_end:
                continue

            else:
                count += 1
                max_end = end
        return count


# @lc code=end
sol = Solution()
res = sol.removeCoveredIntervals(
    [[34335, 39239], [15875, 91969], [29673, 66453], [53548, 69161], [40618, 93111]]
)
print(res)
