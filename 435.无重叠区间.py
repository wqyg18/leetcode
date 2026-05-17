#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
from typing import List


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 每次优先保留结束位置最早的区间。因为结束越早，留给后面区间的空间越大
        intervals.sort(key=lambda x: x[1])
        # 移除的最小数量, 即保留的最大数量
        count = 1
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]

            # 如果当前区间与前一个区间无交集, 就保留
            if start >= end:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count


# @lc code=end
sol = Solution()
res = sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]])
print(res)
