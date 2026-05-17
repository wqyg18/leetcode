#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 找所有区间的交集
        # 因为是要所有的组合, 所以是按照右边界排序

        points.sort(key=lambda x: x[1])

        count = 1
        global_end = points[0][1]

        # 是按照右边界排序的, 所以右边界是越来越大的
        # 现在目标是交集，那么global_end肯定是不会变的，也就是一直是交集中最小的那个
        # 直到出现没有交集
        for i in range(1, len(points)):
            start, end = points[i]
            if start > global_end:
                count += 1
                global_end = end

        return count


# @lc code=end
sol = Solution()
res = sol.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
print(res)
