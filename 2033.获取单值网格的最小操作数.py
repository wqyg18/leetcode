#
# @lc app=leetcode.cn id=2033 lang=python3
#
# [2033] 获取单值网格的最小操作数
#
from typing import List
import math


# @lc code=start
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        base_remainder = grid[0][0] % x
        values = []
        for row in grid:
            for value in row:
                if value % x != base_remainder:
                    return -1
                values.append(value // x)

        # 问题转化为, 求列表中所有元素 values[i] 的最小求和
        # 最小距离是中位数, 而不是均值
        values.sort()
        median = values[len(values) // 2]

        operations = 0
        for value in values:
            operations += abs(value - median)

        return operations


# @lc code=end
sol = Solution()
res = sol.minOperations(grid=[[2, 4], [6, 8]], x=2)
print(res)
